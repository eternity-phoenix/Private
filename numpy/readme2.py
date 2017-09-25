'''
reshape 可以在不改变数组数据的同时，改变数组的形状。其中，numpy.reshape() 等效于 ndarray.reshape()。reshape 方法非常简单：
numpy.reshape(a, newshape)
其中，a 表示原数组，newshape 用于指定新的形状(整数或者元组)。
'''

'''
ravel 的目的是将任意形状的数组扁平化，变为 1 维数组。ravel 方法如下：

numpy.ravel(a, order='C')
其中，a 表示需要处理的数组。order 表示变换时的读取顺序，默认是按照行依次读取，当 order='F' 时，可以按列依次读取排序。
'''

'''
moveaxis 可以将数组的轴移动到新的位置。其方法如下：

numpy.moveaxis(a, source, destination)
其中：

a：数组。
source：要移动的轴的原始位置。
destination：要移动的轴的目标位置。

你可能没有看明白是什么意思，你可以在移动轴之后输出二者的 shape属性对比一下就明白了：
'''

'''
和 moveaxis 不同的是，swapaxes 可以用来交换数组的轴。其方法如下：

numpy.swapaxes(a, axis1, axis2)
其中：

a：数组。
axis1：需要交换的轴 1 位置。
axis2：需要与轴 1 交换位置的轴 1 位置。

同样可以输出前后数组的shape对比一下
'''

'''
transpose 类似于矩阵的转置，它可以将 2 维数组的横轴和纵轴交换。其方法如下：

numpy.transpose(a, axes=None)
其中：

a：数组。
axis：该值默认为 none，表示转置。如果有值，那么则按照值替换轴。
'''

'''
atleast_xd 支持将输入数据直接视为 x维。这里的 x 可以表示：1，2，3。方法分别维：

numpy.atleast_1d()
numpy.atleast_2d()
numpy.atleast_3d()
'''

'''
在 numpy 中，还有一系列以 as 开头的方法，它们可以将特定输入转换为数组，亦可将数组转换为矩阵、标量，ndarray 等。如下：

asarray(a，dtype，order)：将特定输入转换为数组。
asanyarray(a，dtype，order)：将特定输入转换为 ndarray。
asmatrix(data，dtype)：将特定输入转换为矩阵。
asfarray(a，dtype)：将特定输入转换为 float 类型的数组。
asarray_chkfinite(a，dtype，order)：将特定输入转换为数组，检查 NaN 或 infs。
asscalar(a)：将大小为 1 的数组转换为标量。
这里以 asmatrix(data，dtype) 方法举例：
'''
import numpy as np

a = np.arange(4).reshape(2,2)
np.asmatrix(a)

'''
concatenate 可以将多个数组沿指定轴连接在一起。其方法为：

numpy.concatenate((a1, a2, ...), axis=0)
其中：

(a1, a2, ...)：需要连接的数组。
axis：指定连接轴。
举个例子：
'''
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 10]])
c = np.array([[11, 12]])

np.concatenate((a, b, c), axis=0)


'''
在 numpy 中，还有一系列以 as 开头的方法，它们可以将特定输入转换为数组，亦可将数组转换为矩阵、标量，ndarray 等。如下：

stack(arrays，axis)：沿着新轴连接数组的序列。
column_stack()：将 1 维数组作为列堆叠到 2 维数组中。
hstack()：按水平方向堆叠数组。
vstack()：按垂直方向堆叠数组。
dstack()：按深度方向堆叠数组。
这里以 stack(arrays，axis) 方法举例：
'''
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.stack((a, b))

# 当然，也可以横着堆叠。

np.stack((a, b), axis=-1)

'''
split 及与之相似的一系列方法主要是用于数组的拆分，列举如下：

split(ary，indices_or_sections，axis)：将数组拆分为多个子数组。
dsplit(ary，indices_or_sections)：按深度方向将数组拆分成多个子数组。
hsplit(ary，indices_or_sections)：按水平方向将数组拆分成多个子数组。
vsplit(ary，indices_or_sections)：按垂直方向将数组拆分成多个子数组。
下面，我们看一看 split 到底有什么效果：
'''
import numpy as np

a = np.arange(10)
np.split(a, 5)

# 除了 1 维数组，更高维度也是可以直接拆分的。例如，我们可以将下面的数组按行拆分为 2。

import numpy as np

a = np.arange(10).reshape(2,5)
np.split(a, 2)


'''
delete(arr，obj，axis)：沿特定轴删除数组中的子数组。
下面，依次对 4 种方法进行示例，首先是 delete 删除：
'''
import numpy as np

a = np.arange(12).reshape(3,4)
np.delete(a, 2, 1)
# 这里代表沿着横轴，将第 3 列(索引 2)删除。

'''
insert(arr，obj，values，axis)：依据索引在特定轴之前插入值。
再看一看 insert插入, 用法和 delete 很相似，只是需要在第三个参数位置设置需要插入的数组对象：
'''

import numpy as np

a = np.arange(12).reshape(3,4)
b = np.arange(4)

np.insert(a, 2, b, 0)


'''
append(arr，values，axis)：将值附加到数组的末尾，并返回 1 维数组。
append 的用法也非常简单。只需要设置好需要附加的值和轴位置就好了。它其实相当于只能在末尾插入的 insert，所以少了一个指定索引的参数。
'''
import numpy as np

a = np.arange(6).reshape(2,3)
b = np.arange(3)

np.append(a, b)
# 注意 append方法返回值，默认是展平状态下的 1 维数组。

'''
resize(a，new_shape)：对数组尺寸进行重新设定。
resize 就很好理解了，直接举例子吧：
'''
import numpy as np

a = np.arange(10)
a.resize(2,5)
'''
这个 resize 看起来和上面的 reshape 一样呢，都是改变数组原有的形状。

其实，它们直接是有区别的，区别在于对原数组的影响。reshape 在改变形状时，不会影响原数组，相当于对原数组做了一份拷贝。而 resize 则是对原数组执行操作。
'''

'''
在 numpy 中，我们还可以对数组进行翻转操作：

fliplr(m)：左右翻转数组。
flipud(m)：上下翻转数组。
举个例子：
'''
import numpy as np

a = np.arange(16).reshape(4,4)
n.fliplr(a)
n.flipud(a)


'''
numpy.random.rand(d0, d1, ..., dn) 方法的作用为：指定一个数组，并使用 [0, 1) 区间随机数据填充，这些数据均匀分布。
'''
import numpy as np

np.random.rand(2,5)
'''
numpy.random.randn(d0, d1, ..., dn) 与 numpy.random.rand(d0, d1, ..., dn) 的区别在于，返回的随机数据符合标准正太分布。

numpy.random.randint(low, high, size, dtype) 方法将会生成 [low, high) 的随机整数。注意这是一个半开半闭区间。

numpy.random.random_integers(low, high, size) 方法将会生成 [low, high] 的 np.int 类型随机整数。注意这是一个闭区间。

numpy.random.random_sample(size) 方法将会在 [0, 1) 区间内生成指定 size 的随机浮点数。
与 numpy.random.random_sample 类似的方法还有：
numpy.random.random([size])
numpy.random.ranf([size])
numpy.random.sample([size])
它们 4 个的效果都差不多。

'''

'''
numpy.random.choice(a, size, replace, p) 方法将会给定的 1 维数组里生成随机数。
'''
import numpy as np

np.random.choice(10,5)
# 上面的代码将会在 np.arange(10) 中生成 5 个随机数。



'''
除了上面介绍的 6 中随机数生成方法，numpy 还提供了大量的满足特定概率密度分布的样本生成方法。它们的使用方法和上面非常相似，这里就不再一一介绍了。列举如下：

numpy.random.beta(a，b，size)：从 Beta 分布中生成随机数。
numpy.random.binomial(n, p, size)：从二项分布中生成随机数。
numpy.random.chisquare(df，size)：从卡方分布中生成随机数。
numpy.random.dirichlet(alpha，size)：从 Dirichlet 分布中生成随机数。
numpy.random.exponential(scale，size)：从指数分布中生成随机数。
numpy.random.f(dfnum，dfden，size)：从 F 分布中生成随机数。
numpy.random.gamma(shape，scale，size)：从 Gamma 分布中生成随机数。
numpy.random.geometric(p，size)：从几何分布中生成随机数。
numpy.random.gumbel(loc，scale，size)：从 Gumbel 分布中生成随机数。
numpy.random.hypergeometric(ngood, nbad, nsample, size)：从超几何分布中生成随机数。
numpy.random.laplace(loc，scale，size)：从拉普拉斯双指数分布中生成随机数。
numpy.random.logistic(loc，scale，size)：从逻辑分布中生成随机数。
numpy.random.lognormal(mean，sigma，size)：从对数正态分布中生成随机数。
numpy.random.logseries(p，size)：从对数系列分布中生成随机数。
numpy.random.multinomial(n，pvals，size)：从多项分布中生成随机数。
numpy.random.multivariate_normal(mean, cov, size)：从多变量正态分布绘制随机样本。
numpy.random.negative_binomial(n, p, size)：从负二项分布中生成随机数。
numpy.random.noncentral_chisquare(df，nonc，size)：从非中心卡方分布中生成随机数。
numpy.random.noncentral_f(dfnum, dfden, nonc, size)：从非中心 F 分布中抽取样本。
numpy.random.normal(loc，scale，size)：从正态分布绘制随机样本。
numpy.random.pareto(a，size)：从具有指定形状的 Pareto II 或 Lomax 分布中生成随机数。
numpy.random.poisson(lam，size)：从泊松分布中生成随机数。
numpy.random.power(a，size)：从具有正指数 a-1 的功率分布中在 0，1 中生成随机数。
numpy.random.rayleigh(scale，size)：从瑞利分布中生成随机数。
numpy.random.standard_cauchy(size)：从标准 Cauchy 分布中生成随机数。
numpy.random.standard_exponential(size)：从标准指数分布中生成随机数。
numpy.random.standard_gamma(shape，size)：从标准 Gamma 分布中生成随机数。
numpy.random.standard_normal(size)：从标准正态分布中生成随机数。
numpy.random.standard_t(df，size)：从具有 df 自由度的标准学生 t 分布中生成随机数。
numpy.random.triangular(left，mode，right，size)：从三角分布中生成随机数。
numpy.random.uniform(low，high，size)：从均匀分布中生成随机数。
numpy.random.vonmises(mu，kappa，size)：从 von Mises 分布中生成随机数。
numpy.random.wald(mean，scale，size)：从 Wald 或反高斯分布中生成随机数。
numpy.random.weibull(a，size)：从威布尔分布中生成随机数。
numpy.random.zipf(a，size)：从 Zipf 分布中生成随机数。
'''