'''
我们已经知道了，线型图通过 matplotlib.pyplot.plot(*args, **kwargs) 方法绘出。其中，args 代表数据输入，而 kwargs 的部分就是用于设置样式参数了。

二维线型图包含的参数超过 40 余项（文档 P1390）。其中常用的也有 10 余项，选取一些比较有代表性的参数列举如下：

参数	含义
alpha=	设置线型的透明度，从 0.0 到 1.0
color=	设置线型的颜色
fillstyle=	设置线型的填充样式
linestyle=	设置线型的样式
linewidth=	设置线型的宽度
marker=	设置标记点的样式
'''

'''
线型颜色 color = 的预设值（文档 P1527）有：

color =参数值	颜色
b	蓝色
g	绿色
r	红色
w	白色
m	洋红色
y	黄色
k	黑色
……	……
其实，大部分都是所颜色所对应的英文名称首字母。当然，你也可以通过color = '#008000'的方式来设置任何你想要的颜色。
'''

'''
线型的样式 linestyle = 预设的参数值（文档 P1250）有：

linestyle =参数值	线型
'-'	默认实线
'--'	虚线
'-.'	间断线
':'	点状线
参考linestyle.png
'''

'''
样本点标记样式 marker = 预设的参数值（文档 P1527）就更多了：

marker =参数值	样本点标记
'.'	实心点
','	像素点
'o'	空心点
'p'	五角形
'x'	x 形
'+'	+ 形
参考marker.jpg
'''

from matplotlib import pyplot as plt  # 载入 pyplot 绘图模块
import numpy as np  # 载入数值计算模块

# 在 -2PI 和 2PI 之间等间距生成 1000 个值，也就是 X 坐标
X = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
# 计算 sin() 对应的纵坐标
y1 = np.sin(X)
# 计算 cos() 对应的纵坐标
y2 = np.cos(X)

# 向方法中 `*args` 输入 X，y 坐标
plt.plot(X, y1, color='r', linestyle='--', linewidth=2, alpha=0.8)
plt.plot(X, y2, color='b', linestyle='-', linewidth=2)
plt.show()






'''
除了线型图以外，散点图也是常用图形之一。例如，我们在使用机器学习算法聚类的时候，往往就会通过散点图将样本数据展示出来。

Matplotlib 中，绘制散点图的方法我们已经知道了，那就是 matplotlib.pyplot.scatter()。接下来，我们就看一看它包含有哪些参数。

参数	含义
s=	散点大小
c=	散点颜色
marker=	散点样式
cmap=	定义多类别散点的颜色
alpha=	点的透明度
edgecolors=	散点边缘颜色
其中，散点的大小通过设置数值大小控制。散点的颜色可以是一种，参数值和线型的颜色设置类似。散点的颜色也可以是多种，可以使用一个列表对每一个点的颜色单独设置。
'''
from matplotlib import pyplot as plt  # 载入 pyplot 绘图模块
import numpy as np  # 载入数值计算模块

x = np.random.rand(100) # 随机在 0 到 1 之间生成 100 个数值
y = np.random.rand(100) # 随机在 0 到 1 之间生成 100 个数值
colors = np.random.rand(100) # 随机在 0 到 1 之间生成 100 个数值
size = np.random.normal(20, 30, 100) # 随机在 20 到 30 之间生成 100 个数值

# 绘制散点图
plt.scatter(x, y, s=size, c=colors)
plt.show()






'''
饼状图通过 matplotlib.pyplot.pie() 绘出。我们也可以进一步设置它的颜色、标签、阴影等各类样式。
'''
import matplotlib.pyplot as plt

label = 'Cat', 'Dog', 'Cattle', 'Sheep', 'Horse' # 各类别标签
color = 'r', 'g', 'r', 'g', 'y' # 各类别颜色
size = [1, 2, 3, 4, 5] # 各类别占比
explode = (0, 0, 0, 0, 0.2) # 各类别的偏移半径

# 绘制饼状图
plt.pie(size, colors=color, explode=explode, labels=label, shadow=True, autopct='%1.1f%%')

# 饼状图呈正圆
plt.axis('equal')

# 显示图
plt.show()




'''
2.4 组合图

上面演示了三种常见图像的绘制。实际上，我们往往会遇到将几种类型的一样的图放在一张图内显示，也就是组合图的绘制。

其实很简单，你只需要将需要或者的组合图样式放在一起就好了，比如柱形图和折线图。
'''

import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
y_bar = [3, 4, 6, 8, 9, 10, 9, 11, 7, 8]
y_line = [2, 3, 5, 7, 8, 9, 8, 10, 6, 7]

plt.bar(x, y_bar)
plt.plot(x, y_line, '-o', color='y')
plt.show()






'''
2.5 子图绘制

上面提到了组合图绘制，但有一些图是无法组合直接放在一起的，这时就需要子图了。子图，就是将几张独立的图放在一张大图中呈现。在一些需要对比的情形下，子图非常有效。

Matplotlib 中，绘制子图的方法为matplotlib.pyplot.subplot()，我们通过该方法来控制各子图的显示顺序。其中：

subplot(行序号, 列序号, 图序号)
下面列举了三种常见子图的位置关系示意图,参考subplot.jpg
'''
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.linspace(-2*np.pi, 2*np.pi) 

y1 = np.sin(x)
y2 = np.cos(x)

# 子图 1
plt.subplot(2, 2, 1)
plt.plot(x, y1, 'k')
# 子图 2
plt.subplot(2, 2, 2)
plt.plot(x, y2, 'r')
# 子图 3
plt.subplot(2, 2, 3)
plt.plot(x, y2, 'y')
# 子图 4
plt.subplot(2, 2, 4)
plt.plot(x, y2, 'g')

plt.show()
'''
除了这类平行或垂直排列的子图，我们还可以通过 matplotlib.pyplot.subplot()绘制出更复杂的样式。比如，大图套小图。
'''
# axes(rect, axisbg='w') where rect = [left, bottom, width, height] in normalized (0, 1) 
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.linspace(-2 * np.pi, 2 * np.pi)

y1 = np.sin(x)
y2 = np.cos(x)

# 大图
plt.axes([.1, .1, .8, .8])
plt.plot(x, y1, 'k')
# 小图
plt.axes([.6, .6, .3, .3])
plt.plot(x, y2, 'r')

plt.show()




'''
2.6 绘制图例

一般情况下，当绘制好图案后，还需要绘制图例。Matplotlib 中，图例可以通过 matplotlib.pyplot.legend() 方法绘制。
'''
from matplotlib import pyplot as plt  # 载入 pyplot 绘图模块
import numpy as np  # 载入数值计算模块

# 生成数据
X = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y1 = np.sin(X)
y2 = np.cos(X)

# 使用 label= 添加标签
plt.plot(X, y1, color='r', linestyle='--', linewidth=2, label='sin 函数')
plt.plot(X, y2, color='b', linestyle='-', linewidth=2, label='cos 函数')
# 绘制图例
plt.legend(loc='upper left')
plt.show()
'''
在这里，我们需要修改两个地方，也就是通过 label= 为每一条曲线添加标签。
然后，增加一条 plt.legend(loc='upper left') 就可以了。其中，loc='upper left' 是指明图例的位置，例如这里是左上方。你还可以通过 down 和 right 组合实现位置的变换。
'''





'''
2.7 图像标注

当我们绘制一些较为复杂的图像时，阅读对象往往很难全面理解图像的含义。而此时，图像标注往往会起到画龙点睛的效果。图像标注，就是在画面上添加文字注释、指示箭头、图框等各类标注元素。

Matplotlib 中，文字标注的方法由 matplotlib.pyplot.text() 实现。最基本的样式为 matplotlib.pyplot.text(x, y, s)，其中 x, y 用于标注位置定位，s 代表标注的字符串。除此之外，你还可以通过 fontsize= , horizontalalignment= 等参数调整标注字体的大小，对齐样式等。
'''
from matplotlib import pyplot as plt # 载入绘图模块

x_bar = [10, 20, 30, 40, 50] #柱形图横坐标
y_bar = [0.5, 0.6, 0.7, 0.4, 0.6] #柱形图纵坐标
bars = plt.bar(x_bar, y_bar, color='blue', label=x_bar, width=2) # 绘制柱形图
for i, rect in enumerate(bars):
    x_text = rect.get_x() # 获取柱形图横坐标
    y_text = rect.get_height() + 0.01 # 获取柱子的高度并增加 0.01
    plt.text(x_text, y_text, '%.1f' % y_bar[i]) # 标注文字

plt.show()

'''
下面的示例中，xy=() 表示标注终点坐标，xytext=() 表示标注起点坐标。
另外，arrowprops=() 用于设置箭头样式，facecolor= 设置颜色，width= 设置箭尾宽度，headwidth= 设置箭头宽度。

在箭头绘制的过程中，还有一个 arrowstyle= 用于改变箭头的样式。参考图arrowstyle.png

另外，connectionstyle= 的参数可以用于更改箭头连接的样式。参考图connectionstyle.png
'''
# 除了文字标注之外，还可以通过 matplotlib.pyplot.annotate() 方法向图像中添加箭头等样式标注。
from matplotlib import pyplot as plt # 载入绘图模块

x_bar = [10, 20, 30, 40, 50] #柱形图横坐标
y_bar = [0.5, 0.6, 0.7, 0.4, 0.6] #柱形图纵坐标
bars = plt.bar(x_bar, y_bar, color='blue', label=x_bar, width=2) # 绘制柱形图
for i, rect in enumerate(bars):
    x_text = rect.get_x() # 获取柱形图横坐标
    y_text = rect.get_height() + 0.01 # 获取柱子的高度并增加 0.01
    plt.text(x_text, y_text, '%.1f' % y_bar[i]) # 标注文字

    # 增加箭头标注
    plt.annotate('Max', xy=(32, 0.6), xytext=(38, 0.6), arrowprops=dict(facecolor='black', width=1, headwidth=7))

plt.show()






'''
2.8 动态图绘制

动态图是绘图中不可缺少的一部分，虽然演示环境要求高且使用频率低，但在一些特定的场景下，动图传达的信息量远大于静态图片。

举个例子来讲，数值计算中，我们往往会使用到梯度下降法。如果用语言和公式描述梯度下降的过程，会非常枯燥。要是通过绘制一张演示梯度下降过程的动图，就算第一次接触该方法，也会很快的理解。

Matplotlib 很早开始就支持动态图了，下面就通过简单的小例子来演示一下动态图的绘制。

动态图主要是通过 animation 模块实现。具体就是 matplotlib.animation.FuncAnimation(fig, func)。其中，fig 代表所绘制的图像。而 func 可以看作是更新函数，它刷新每一帧的值。
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 生成数据并建立绘制类型的图像
fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)

line, = plt.plot(x, np.sin(x))

# 更新函数
def update(i):
    line.set_ydata(np.sin(x + i / 10.0))
    return line,

# 绘制动图
animation = animation.FuncAnimation(fig, update)

# 显示图
plt.show()

# 实例
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5), dpi=80)
ax = plt.subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="Cos Function")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="Sin Function")

plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.ylim(C.min() * 1.1, C.max() * 1.1)
plt.yticks([-1, +1],
           [r'$-1$', r'$+1$'])

t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)],
         color='blue', linewidth=1.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t], [0, np.sin(t)],
         color='red', linewidth=1.5, linestyle="--")
plt.scatter([t, ], [np.sin(t), ], 50, color='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.legend(loc='upper left', frameon=False)
plt.show()