# 一维数据索引：

import numpy as np

a = np.arange(10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 获取索引值为 1 的数据
a[1]
# 分别获取索引值为 1，2，3 的数据
a[[1, 2, 3]]
array([1, 2, 3])

# 对于二维数据而言：

import numpy as np

a = np.arange(20).reshape(4,5)

# 获取第 2 行，第 3 列的数据
a[1,2]

# 如何索引二维 Ndarray 中的多个元素值，这里使用逗号,分割：

import numpy as np

a = np.arange(20).reshape(4,5)
# 索引
a[[1,2],[3,4]]
array([ 8, 14])
# 这里需要注意索引的对应关系。我们实际获取的是[1,3]，也就是第2行和第4列对于的值8。以及[2, 4]，也就是第3行和第5列对于的值14。

# 三维数据
a = np.arange(30).reshape(2,5,3)

# 索引
a[[0,1],[1,2],[1,2]]
array([ 4, 23])
# 这里，[0,1]分布代表 axis = 0 和 axis = 1。而，后面的[1,2],[1,2] 分别选择了第 2 行第2 列和第 3 行第3 列的两个数。



'''
Numpy 里面针对Ndarray的数组切片和 python 里的list 切片操作是一样的。其语法为：

Ndarray[start:stop:step]
start:stop:step 分布代表起始索引：截至索引：步长。对于一维数组：
'''
>> import numpy as np

a = np.arange(10)
a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a[:5]
array([0, 1, 2, 3, 4])

a[5:10]
array([5, 6, 7, 8, 9])

a[0:10:2]
array([0, 2, 4, 6, 8])

# 对于多维数组，我们只需要用逗号,分割不同维度即可：

import numpy as np

a = np.arange(20).reshape(4,5)

# 先取第 3，4 列（第一个维度），再取第 1，2，3 行（第二个维度）。
a[0:3,2:4]

# 按步长为 2 取所有列和所有行的数据。
a[:,::2]

# 当超过 3 维或更多维时，用 2 维数据的切片方式类推即可。

# 修改切片中的内容会影响原始数组。




'''
最后，再介绍几个 numpy 针对数组元素的使用方法，分别是排序、搜索和计数。

3.1 排序

我们可以使用 numpy.sort方法对多维数组元素进行排序。其方法为：

numpy.sort(a, axis=-1, kind='quicksort', order=None)
其中：

a：数组。
axis：要排序的轴。如果为None，则在排序之前将数组铺平。默认值为 -1，沿最后一个轴排序。
kind：{'quicksort'，'mergesort'，'heapsort'}，排序算法。默认值为 quicksort。

除了 numpy.sort，还有这样一些对数组进行排序的方法：

numpy.lexsort(keys ,axis)：使用多个键进行间接排序。
numpy.argsort(a ,axis,kind,order)：沿给定轴执行间接排序。
numpy.msort(a)：沿第 1 个轴排序。
numpy.sort_complex(a)：针对复数排序。
'''



'''
除了排序，我们可以通过下面这些方法对数组中元素进行搜索和计数。列举如下：

argmax(a ,axis,out)：返回数组中指定轴的最大值的索引。
nanargmax(a ,axis)：返回数组中指定轴的最大值的索引,忽略 NaN。
argmin(a ,axis,out)：返回数组中指定轴的最小值的索引。
nanargmin(a ,axis)：返回数组中指定轴的最小值的索引,忽略 NaN。
argwhere(a)：返回数组中非 0 元素的索引,按元素分组。
nonzero(a)：返回数组中非 0 元素的索引。
flatnonzero(a)：返回数组中非 0 元素的索引,并铺平。
where(条件,x,y)：根据指定条件,从指定行、列返回元素。
searchsorted(a,v ,side,sorter)：查找要插入元素以维持顺序的索引。
extract(condition,arr)：返回满足某些条件的数组的元素。
count_nonzero(a)：计算数组中非 0 元素的数量。
'''

a = np.random.randint(0,10,20)
array([3, 2, 0, 4, 3, 1, 5, 8, 4, 6, 4, 5, 4, 2, 6, 6, 4, 9, 8, 9])

np.argmax(a)
17

np.nanargmax(a)
17

np.argmin(a)
2

np.nanargmin(a)
2

np.argwhere(a)
array([[ 0],[ 1],[ 3],[ 4],[ 5],[ 6],[ 7],[ 8],[ 9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19]], dtype=int64)

np.nonzero(a)
(array([ 0,  1,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], dtype=int64),)

np.flatnonzero(a)
array([ 0,  1,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], dtype=int64)

np.count_nonzero(a)
19