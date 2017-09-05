'''
其实，Matplotlib 也可以绘制 3D 图像，与二维图像不同的是，绘制三维图像主要通过 mplot3d 模块实现。但是，使用 Matplotlib 绘制三维图像实际上是在二维画布上展示，
所以一般绘制三维图像时，同样需要载入 pyplot 模块。

mplot3d 模块下主要包含 4 个大类，分别是：

mpl_toolkits.mplot3d.axes3d()
mpl_toolkits.mplot3d.axis3d()
mpl_toolkits.mplot3d.art3d()
mpl_toolkits.mplot3d.proj3d()
其中，axes3d() 下面主要包含了各种实现绘图的类和方法。axis3d() 主要是包含了和坐标轴相关的类和方法。
art3d() 包含了一些可将 2D 图像转换并用于 3D 绘制的类和方法。
proj3d() 中包含一些零碎的类和方法，例如计算三维向量长度等。

一般情况下，我们用到最多的就是 mpl_toolkits.mplot3d.axes3d 下面的 mpl_toolkits.mplot3d.axes3d.Axes3D() 类，而 Axes3D() 下面又存在绘制不同类型 3D 图的方法。
你可以通过下面的方式导入 Axes3D()。
'''
from mpl_toolkits.mplot3d.axes3d import Axes3D
# 也可以使用下面的方式导入
# from mpl_toolkits.mplot3d import Axes3D


'''
三维散点图
'''
import numpy as np

# x, y, z 均为 0 到 1 之间的 100 个随机数
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
z = np.random.normal(0, 1, 100)

# 接下来，开始绘图。第一步是载入 2D, 3D 绘图模块。
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# 第二步，使用 Axes3D() 创建 3D 图形对象。
fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(x, y, z)

plt.show()


# 线形图和散点图相似，需要传入 x, y, z 三个坐标的数值。
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(-6 * np.pi, 6 * np.pi, 1000)
y = np.sin(x)
z = np.cos(x)

# 创建 3D 图形对象
fig = plt.figure()
ax = Axes3D(fig)

# 绘制线型图
ax.plot(x, y, z)

# 显示图
plt.show()


# 我们继续尝试绘制三维柱状图，其实它的绘制步骤和上面同样非常相似。
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# 创建 3D 图形对象
fig = plt.figure()
ax = Axes3D(fig)

# 生成数据并绘图
x = [0, 1, 2, 3, 4, 5, 6]
for i in x:
    y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    z = abs(np.random.normal(1, 10, 10))
    ax.bar(y, z, i, zdir='y', color=['r', 'g', 'b', 'y'])

plt.show()




'''
需要绘制的三维曲面图要麻烦一些，我们需要对数据进行矩阵处理。其实和画二维等高线图很相似，只是多增加了一个维度。
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建 3D 图形对象
fig = plt.figure()
ax = Axes3D(fig)

# 生成数据
X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(X ** 2 + Y ** 2)

# 绘制曲面图，并使用 cmap 着色
ax.plot_surface(X, Y, Z, cmap=plt.cm.winter)

plt.show()
# cmap=plt.cm.winter 表示采用了 winter 配色方案，也就是下图的渐变色。



'''
混合图就是将两种不同类型的图绘制在一张图里。绘制混合图一般有前提条件，那就是两种不同类型图的范围大致相同，否则将会出现严重的比例不协调，而使得混合图失去意义。
'''
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# 创建 3D 图形对象
fig = plt.figure()
ax = Axes3D(fig)

# 生成数据并绘制图 1
x1 = np.linspace(-3 * np.pi, 3 * np.pi, 500)
y1 = np.sin(x1)
ax.plot(x1, y1, zs=0, c='red')

# 生成数据并绘制图 2
x2 = np.random.normal(0, 1, 100)
y2 = np.random.normal(0, 1, 100)
z2 = np.random.normal(0, 1, 100)
ax.scatter(x2, y2, z2)

# 显示图
plt.show()


'''
子图绘制
我们可以将二维图像和三维图像绘制在一起，又或者将几个三维图像绘制在一起。
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# 创建 1 张画布
fig = plt.figure()

#===============

# 向画布添加子图 1 
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# 生成子图 1 数据
x = np.linspace(-6 * np.pi, 6 * np.pi, 1000)
y = np.sin(x)
z = np.cos(x)

# 绘制第 1 张图
ax1.plot(x, y, z)

#===============

# 向画布添加子图 2
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# 生成子图 2 数据
X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(X ** 2 + Y ** 2)

# 绘制第 2 张图
ax2.plot_surface(X, Y, Z, cmap=plt.cm.winter)

# 显示图
plt.show()
# 我们可以来看一下这些代码。由于两张子图是绘制在 1 张画布上面的，所以这里需要提前创建 1 张画布。然后通过 .add_subplot() 添加子图，子图序号和二维绘图相似，只是注意 3D 绘图时要添加 projection='3d' 参数。
