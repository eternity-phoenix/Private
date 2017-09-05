#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib
from matplotlib import pyplot as plt

plt.plot([1,2,3,2,1,2,3,4,5,6,5,4,3,2,1])
plt.show()
'''
上文中，我们提到了 pyplot 模块，其中 pyplot.plot 方法是用来绘制折线图的。
你应该会很容易联想到，更改后面的方法类名就可以更改图形的样式，会是这样的吗？

的确，在 Matplotlib 中，大部分图形样式的绘制方法都存在于 pyplot 模块中。例如：
'''
matplotlib.pyplot.angle_spectrum            # 绘制电子波谱图
matplotlib.pyplot.bar                       # 绘制柱状图
matplotlib.pyplot.barh                      # 绘制直方图
matplotlib.pyplot.broken_barh               # 绘制水平直方图
matplotlib.pyplot.contour                   # 绘制等高线图
matplotlib.pyplot.errorbar                  # 绘制误差线
matplotlib.pyplot.hexbin                    # 绘制六边图案
matplotlib.pyplot.hist	                    # 绘制柱形图
matplotlib.pyplot.hist2d	                # 绘制水平柱状图
matplotlib.pyplot.imshow	                # 以图像显示
matplotlib.pyplot.pie	                    # 绘制饼状图
matplotlib.pyplot.quiver	                # 绘制量场图
matplotlib.pyplot.scatter	                # 散点图
matplotlib.pyplot.specgram	                # 绘制光谱图
matplotlib.pyplot.subplot	                # 绘制子图

'除此之外，对图像样式的微调，包括标注、填充、自定义坐标轴等也同样包含在 pyplot 模块中。'
matplotlib.pyplot.annotate	                # 绘制图形标注
matplotlib.pyplot.axhspan	                # 绘制垂直或水平色块
matplotlib.pyplot.clabel	                # 标注轮廓线
matplotlib.pyplot.fill	                    # 填充区域

'''
方法：matplotlib.pyplot.plot(*args, **kwargs)

上面我们见到使用该方法来绘制折线图。其实，matplotlib.pyplot.plot(*args, **kwargs)方法严格来讲可以绘制线型图或者样本标记。
其中，*args允许输入单个 y 值或 x,y 值。
'''
from matplotlib import pyplot as plt #载入 pyplot 绘图模块
import numpy as np # 载入数值计算模块

# 在 -2PI 和 2PI 之间等间距生成 1000 个值，也就是 X 坐标
X = np.linspace(-2*np.pi, 2*np.pi, 1000)
# 计算 y 坐标
y = np.sin(X)

# 向方法中 `*args` 输入 X，y 坐标
plt.plot(X, y)
plt.show()




'''
方法：matplotlib.pyplot.bar(*args, **kwargs)
'''
from matplotlib import pyplot as plt #载入 pyplot 绘图模块
import numpy as np # 载入数值计算模块

# 在 -2PI 和 2PI 之间等间距生成 10 个值，也就是 X 坐标
X = np.linspace(-2*np.pi, 2*np.pi, 10)
# 计算 y 坐标
y = np.sin(X)

# 向方法中 `*args` 输入 X，y 坐标
plt.bar(X, abs(y))  # y 值取绝对值
plt.show()



'''
方法：matplotlib.pyplot.scatter(*args, **kwargs)

散点图就是呈现在二维平面的一些点，这种图像的需求也是非常常见的。比如，我们通过 GPS 采集的数据点，它会包含经度以及纬度两个值，这样的情况就可以绘制成散点图。
'''
from matplotlib import pyplot as plt #载入 pyplot 绘图模块
import numpy as np # 载入数值计算模块

# X,y 的坐标均有 numpy 在 0 到 1 中随机生成 1000 个值
X = np.random.ranf(1000)
y = np.random.ranf(1000)

# 向方法中 `*args` 输入 X，y 坐标
plt.scatter(X, y)
plt.show()



'''
方法：matplotlib.pyplot.pie(*args, **kwargs)

饼状图在有限列表以百分比呈现时特别有用，你可以很清晰地看出来各类别之间的大小关系，以及各类别占总体的比例。
'''
from matplotlib import pyplot as plt #载入 pyplot 绘图模块

Z = [1, 2, 3, 4, 5]
# 绘图
plt.pie(Z)
plt.show()
# 这里的 Z 值反映了互相之间的大小关系，而无论输入多少个值，最终都是在一张饼（100%）里瓜分。



'''
方法：matplotlib.pyplot.quiver(*args, **kwargs)

量场图就是由向量组成的图像，在气象学等方面被广泛应用。从图像的角度来看，量场图就是带方向的箭头符号。
'''
from matplotlib import pyplot as plt #载入 pyplot 绘图模块
import numpy as np # 载入数值计算模块

# 生成数据矩阵
X, y = np.mgrid[0:10, 0:10]
# 绘图
plt.quiver(X, y)
plt.show()



'''
方法：matplotlib.pyplot.contourf(*args, **kwargs)

中学学习地理的时候，我们就知道等高线了。等高线图是工程领域经常接触的一类图，
'''
from matplotlib import pyplot as plt #载入 pyplot 绘图模块
import numpy as np # 载入数值计算模块

# 生成数据
x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)
X, Y = np.meshgrid(x, y)
Z = (1 - X / 2 + X ** 3 + Y ** 4) * np.exp(-X ** 2 - Y ** 2)

# 绘图
plt.contourf(X, Y, Z)
plt.show()
'''
值得注意的是，当我们向 contourf(X,Y,Z) 传入数据时，一定要注意相互之间的维度关系，不然很容易报错。其中，当 X,Y,Z 都是 2 维数组时，它们的形状必须相同。
如果都是 1 维数组时，len(X)是 Z 的列数，而 len(Y) 是 Z 中的行数。
'''





