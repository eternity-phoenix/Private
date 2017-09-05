'''
Seaborn 基于 Matplotlib 核心库进行了更高级的 API 封装，可以让你轻松地画出更漂亮的图形。而 Seaborn 的漂亮主要体现在配色更加舒服、以及图形元素的样式更加细腻。
'''
'''
我们列举一下 Seaborn 的几个特点：

内置数个经过优化的样式效果。
增加调色板工具，可以很方便地为数据搭配颜色。
单变量和双变量分布绘图更为简单，可用于对数据子集相互比较。
对独立变量和相关变量进行回归拟合和可视化更加便捷。
对数据矩阵进行可视化，并使用聚类算法进行分析。
基于时间序列的绘制和统计功能，更加灵活的不确定度估计。
基于网格绘制出更加复杂的图像集合。
除此之外， Seaborn 对 Matplotlib 和 Pandas 的数据结构高度兼容 ，非常适合作为数据挖掘过程中的可视化工具。
'''

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns # 导入 seaborn 模块

x = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
y_bar = [3, 4, 6, 8, 9, 10, 9, 11, 7, 8]
y_line = [2, 3, 5, 7, 8, 9, 8, 10, 6, 7]

sns.set() # 使用 set() 方法 1 步设置默认样式
# 注意，sns.set() 样式设置语句需要放置在 Matplotlib 原本的绘图语句前面。

plt.bar(x, y_bar)
plt.plot(x, y_line, '-o', color='y')

plt.show()
'''
这里，sns.set() 采用了默认参数，分别为：

sns.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=False, rc=None)

context='' 参数控制着默认的画幅大小，分别有 {paper, notebook, talk, poster} 四个值。其中，poster > talk > notebook > paper。
style='' 参数控制默认样式，分别有 {darkgrid, whitegrid, dark, white, ticks}，你可以自行更改查看它们之间的不同。
palette='' 参数为预设的调色板。分别有 {deep, muted, bright, pastel, dark, colorblind} 等，你可以自行更改查看它们之间的不同。
剩下的 font='' 用于设置字体，font_scale= 设置字体大小，color_codes= 不使用调色板而采用先前的 'r' 等色彩缩写。
'''





'''
3.2 seaborn.lmplot()

seaborn.lmplot() 是一个非常有用的方法，它会在绘制二维散点图时，自动完成回归拟合。我们拿 UCI 提供的 iris 鸢尾花数据集举例。
数据集总共 150 行，由 5 列组成。分别代表：萼片长度、萼片宽度、花瓣长度、花瓣宽度、花的类别。其中，前四列均为数值型数据，最后一列花的分类为三种，分别是：Iris Setosa、Iris Versicolour、Iris Virginica。
'''

import seaborn as sns  #载入 seaborn 模块

iris_data = sns.load_dataset('iris')  # 导入 iris 数据集

# 我们尝试通过 seaborn.lmplot() 将第一列和第二列绘制为散点图。
print(iris_data)
sns.lmplot(x='sepal_length', y='sepal_width', hue='species', data=iris_data)
plt.show()

'''
sns.lmplot() 里的 x, y 分别代表横纵坐标的列名。hue= 代表按照 species，即花的类别分类显示，而 data= 自然就是关联到数据集了。
'''




'''
3.3 seaborn.PairGrid

seaborn.PairGrid() 可以用来查看两个维度数据之间的关系，用处当然也非常多了。比如，方便我们在数据分析过程中找出强关联特征。
'''
# 绘图
sns.PairGrid(data=iris_data, hue='species').map(plt.scatter)
plt.show()
'''
seaborn.PairGrid() 用法非常简单，只需要将整个数据集放进去，然后使用 seaborn.PairGrid().map() 设置绘图的样式，比如这里选择了 scatter 散点图。
Seaborn 自动将 4 个维度的数值型数据进行两两配对，绘制除了 16 张散点图。

如果你认为一种颜色不好看，那么只需要像上面一样，添加 hue= 参数即可。比如，这里按照花的类别显示。
'''




'''
3.4 seaborn.PairGrid

seaborn.PairGrid() 可以绘制出单变量和双变量的组合图，
'''
# 绘图
sns.JointGrid(data=iris_data, x='sepal_length', y='sepal_width')
plt.show()
# 你会发现，这样绘制出来是一张空白图。原因是我们没有选择图的样式。
# sns.JointGrid().plot() 用于设置图形的样式。我们将中间的图选为双变量的散点图，而上面和右面选为单变量的直方图。
sns.JointGrid(data=iris_data, x='sepal_length', y='sepal_width').plot(sns.regplot, sns.distplot)
plt.show()




'''
3.5 seaborn.kdeplot

seaborn.kdeplot() 主要是用于绘制单变量或二元变量的核密度估计图。先看看单变量的效果。
'''
# 绘图
sns.kdeplot(data=iris_data["sepal_length"])

plt.show()
# 绘制单变量时，直接将一维数组输入即可。

'''
你可以通过 kernel= 参数设置核函数，有 {'gau' | 'cos' | 'biw' | 'epa' | 'tri' | 'triw' }等，默认为 kernel='gau'。还可以通过其他参数更改绘制的效果，
'''
sns.kdeplot(data=iris_data["sepal_length"], shade=True, color='y')

plt.show()

# 对于二元变量来讲，就是再再输入一个一维数组即可。
sns.kdeplot(data=iris_data["sepal_length"], data2=iris_data["sepal_width"], shade=True)

plt.show()




'''
3.6 seaborn.heatmap

seaborn.heatmap() 主要是用于绘制热力图，也就类似于色彩矩阵。
'''
# 生成 10x10 的随机矩阵
matrix_data = np.random.rand(10, 10)

# 绘图
sns.heatmap(data=matrix_data)

plt.show()




'''
3.7 seaborn.clustermap

seaborn.clustermap() 可以将矩阵数据集绘制为层次聚类热图。
'''
iris_data.pop("species")  #去掉了花的类别列

# 绘图
sns.clustermap(iris_data)
plt.show()