
'''
Numpy 支持比 Python 本身更为丰富的数值类型，细分如下：

bool：布尔类型，1 个字节，值为 True 或 False。
int：整数类型，通常为 int64 或 int32 。
intc：与 C 里的 int 相同，通常为 int32 或 int64。
intp：用于索引，通常为 int32 或 int64。
int8：字节（从 -128 到 127）
int16：整数（从 -32768 到 32767）
int32：整数（从 -2147483648 到 2147483647）
int64：整数（从 -9223372036854775808 到 9223372036854775807）
uint8：无符号整数（从 0 到 255）
uint16：无符号整数（从 0 到 65535）
uint32：无符号整数（从 0 到 4294967295）
uint64：无符号整数（从 0 到 18446744073709551615）
float：float64 的简写。
float16：半精度浮点，5 位指数，10 位尾数
float32：单精度浮点，8 位指数，23 位尾数
float64：双精度浮点，11 位指数，52 位尾数
complex：complex128 的简写。
complex64：复数，由两个 32 位浮点表示。
complex128：复数，由两个 64 位浮点表示。
在 Numpy 中，上面提到的这些数值类型都被归于 dtype（data-type） 对象的实例。

我们可以用 numpy.dtype(object, align, copy) 来指定数值类型。而在数组里面，可以用 dtype= 参数。
'''

import numpy as np

a = np.array([1.1, 2.2, 3.3], dtype=np.float64) # 指定 1 维数组的数值类型为 float64

# 另外，你可以使用 .astype() 方法在不同的数值类型之间相互转换。

a.astype(int) # 将 a 的数值类型从 float64 转换为 int

# 最后，你可以使用 .dtype 来查看 dtype 属性。

a.dtype # 查看 a 的数值类型



'''
python 标准类针对数组的处理局限于 1 维，并仅提供少量的功能。

而 Numpy 最核心且最重要的一个特性就是 ndarray 多维数组对象，它区别于 python 的标准类，拥有对高维数组的处理能力，这也是数值计算过程中缺一不可的重要特性。

Numpy 中，ndarray 类具有六个参数，它们分别为：

shape：数组的形状。
dtype：数据类型。
buffer：对象暴露缓冲区接口。
offset：数组数据的偏移量。
strides：数据步长。
order：{'C'，'F'}，以行或列为主排列顺序。
'''

'''
在 numpy 中，我们使用 numpy.array 将列表或元组转换为 ndarray 数组。其方法为：

numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
其中，参数：

object：列表、元组等。
dtype：数据类型。如果未给出，则类型为被保存对象所需的最小类型。
copy：布尔来写，默认 True，表示复制对象。
order：顺序。
subok：布尔类型，表示子类是否被传递。
ndmin：生成的数组应具有的最小维数。
'''

'''
arange() 的功能是在给定区间内创建一系列均匀间隔的值。方法如下：

numpy.arange(start, stop, step, dtype=None)
你需要先设置值所在的区间，这里为 `[开始， 停止），你应该能发现这是一个半开半闭区间。然后，在设置 step 步长用于设置值之间的间隔。最后的可选参数 dtype可以设置返回ndarray 的值类型。
'''

'''
linspace方法也可以像arange方法一样，创建数值有规律的数组。linspace 用于在指定的区间内返回间隔均匀的值。其方法如下：

numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
start：序列的起始值。
stop：序列的结束值。
num：生成的样本数。默认值为50。
endpoint：布尔值，如果为真，则最后一个样本包含在序列内。
retstep：布尔值，如果为真，返回间距。
dtype：数组的类型。
'''

'''
numpy.ones 用于快速创建数值全部为 1 的多维数组。其方法如下：

numpy.ones(shape, dtype=None, order='C')
其中：

shape：用于指定数组形状，例如（1， 2）或 3。
dtype：数据类型。
order：{'C'，'F'}，按行或列方式储存数组。
'''

'''
zeros 方法和上面的 ones 方法非常相似，不同的地方在于，这里全部填充为 0。zeros 方法和 ones 是一致的。

numpy.zeros(shape, dtype=None, order='C')
其中：

shape：用于指定数组形状，例如（1， 2）或3。
dtype：数据类型。
order：{'C'，'F'}，按行或列方式储存数组。
'''

'''
numpy.eye 用于创建一个二维数组，其特点是k 对角线上的值为 1，其余值全部为0。方法如下：

numpy.eye(N, M=None, k=0, dtype=<type 'float'>)
其中：

N：输出数组的行数。
M：输出数组的列数。
k：对角线索引：0（默认）是指主对角线，正值是指上对角线，负值是指下对角线。
'''

'''
我们还可以从已知数据文件、函数中创建 ndarray。numpy 提供了下面 5 个方法：

frombuffer（buffer）：将缓冲区转换为 1 维数组。
fromfile（file，dtype，count，sep）：从文本或二进制文件中构建多维数组。
fromfunction（function，shape）：通过函数返回值来创建多维数组。
fromiter（iterable，dtype，count）：从可迭代对象创建 1 维数组。
fromstring（string，dtype，count，sep）：从字符串中创建 1 维数组。
'''


'''
ndarray.T用于数组的转置，与 .transpose() 相同。

ndarray.dtype 用来输出数组包含元素的数据类型。

ndarray.imag 用来输出数组包含元素的虚部。

ndarray.real用来输出数组包含元素的实部。

ndarray.size用来输出数组中的总包含元素数。

ndarray.itemsize输出一个数组元素的字节数。

ndarray.nbytes用来输出数组的元素总字节数。

ndarray.ndim用来输出数组尺寸。

ndarray.shape用来输出数组维数组.

ndarray.strides用来遍历数组时，输出每个维度中步进的字节数组。
'''



