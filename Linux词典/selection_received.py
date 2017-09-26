'''
GTK中有各种各样的事件，比如按钮点击事件，选择事件等。又由于GTK中的控件没有X window，所以这些控件本身不具有接收事件的功能。
在GTK中如果要让控件接收到事件，必须要先生成一个事件容器控件，然后让控件附加到这个事件容器 中。
我们开发的词典程序，会翻译我们选择到的单词，那程序是如何检测到选择到的单词的呢？这就需要selection_received事件了，
同时获取 选择事件是一个异步过程，所以要获取选择事件，需要先执行widget.selection_convert()方法。
'''

import pygtk
pygtk.require(‘2.0‘)
import gtk

class GetSelectionExample(object):

    def __init__(self):
        # 创建窗口
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Get Selection")
        window.set_border_width(10)
        window.connect("destroy", lambda w: gtk.main_quit())

        # 创建一个垂直容器
        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()

        # 创建了一个按钮，当用点击按钮的时候，触发self.get_stringtarget函数
        button = gtk.Button(u"输出选择字符串")
        eventbox = gtk.EventBox()
        eventbox.add(button)
        button.connect_object("clicked", self.get_stringtarget, eventbox)
        eventbox.connect("selection_received", self.selection_received)
        vbox.pack_start(eventbox)
        eventbox.show()
        button.show()

        window.show()

    def get_stringtarget(self, widget):
        # 开始获取选择的字符串
        widget.selection_convert("PRIMARY", "STRING")
        return
    
    '''
    clicked事件，触发了selection_convert函数，然后该函数检查成功后触发了selection_received 事件。
    '''
    def selection_received(self, widget, selection_data, data):
        # 开始解析出获取到的字符串
        if str(selection_data.type) == "STRING":
            # 打印获取到的字符串
            print(u"被选择的字符串: " + selection_data.get_text())

        elif str(selection_data.type) == "ATOM":
            # Print out the target list we received
            targets = selection_data.get_targets()
            for target in targets:
                name = str(target)
                if name is not None:
                    print("%s" % name)
                else:
                    print("(bad target)")
        else:
            print("Selection was not returned as \"STRING\" or \"ATOM\"!")

        return False


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    GetSelectionExample()
    main()