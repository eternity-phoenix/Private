'''
numpy 提供的三角函数功能。这些方法有：
numpy.sin(x)：三角正弦。
numpy.cos(x)：三角余弦。
numpy.tan(x)：三角正切。
numpy.arcsin(x)：三角反正弦。
numpy.arccos(x)：三角反余弦。
numpy.arctan(x)：三角反正切。
numpy.hypot(x1,x2)：直角三角形求斜边。
numpy.degrees(x)：弧度转换为度。
numpy.radians(x)：度转换为弧度。
numpy.deg2rad(x)：度转换为弧度。
numpy.rad2deg(x)：弧度转换为度。


在数学中，双曲函数是一类与常见的三角函数类似的函数。双曲函数经常出现于某些重要的线性微分方程的解中，使用 numpy 计算它们的方法为：
numpy.sinh(x)：双曲正弦。
numpy.cosh(x)：双曲余弦。
numpy.tanh(x)：双曲正切。
numpy.arcsinh(x)：反双曲正弦。
numpy.arccosh(x)：反双曲余弦。
numpy.arctanh(x)：反双曲正切。
'''

'''
数值修约, 又称数字修约, 是指在进行具体的数字运算前, 按照一定的规则确定一致的位数, 然后舍去某些数字后面多余的尾数的过程[via. 维基百科]。比如, 我们常听到的「4 舍 5 入」就属于数值修约中的一种。
numpy.around(a)：平均到给定的小数位数。
numpy.round_(a)：将数组舍入到给定的小数位数。
numpy.rint(x)：修约到最接近的整数。
numpy.fix(x, y)：向 0 舍入到最接近的整数。
numpy.floor(x)：返回输入的底部(标量 x 的底部是最大的整数 i)。
numpy.ceil(x)：返回输入的上限(标量 x 的底部是最小的整数 i).
numpy.trunc(x)：返回输入的截断值。
'''
import numpy as np

a = np.array([1.21, 2.53, 3.86])
# array([ 1.21,  2.53,  3.86])

np.around(a)
# array([ 1.,  3.,  4.])

np.round_(a)
# array([ 1.,  3.,  4.])

np.rint(a)
# array([ 1.,  3.,  4.])

np.fix(a)
# array([ 1.,  2.,  3.])

np.floor(a)
# array([ 1.,  2.,  3.])

np.ceil(a)
# array([ 2.,  3.,  4.])

np.trunc(a)
# array([ 1.,  2.,  3.])



'''
下面这些方法用于数组内元素或数组间进行求和、求积以及进行差分。

numpy.prod(a, axis, dtype, keepdims)：返回指定轴上的数组元素的乘积。
numpy.sum(a, axis, dtype, keepdims)：返回指定轴上的数组元素的总和。
numpy.nanprod(a, axis, dtype, keepdims)：返回指定轴上的数组元素的乘积, 将 NaN 视作 1。
numpy.nansum(a, axis, dtype, keepdims)：返回指定轴上的数组元素的总和, 将 NaN 视作 0。
numpy.cumprod(a, axis, dtype)：返回沿给定轴的元素的累积乘积。
numpy.cumsum(a, axis, dtype)：返回沿给定轴的元素的累积总和。
numpy.nancumprod(a, axis, dtype)：返回沿给定轴的元素的累积乘积, 将 NaN 视作 1。
numpy.nancumsum(a, axis, dtype)：返回沿给定轴的元素的累积总和, 将 NaN 视作 0。
numpy.diff(a, n, axis)：计算沿指定轴的第 n 个离散差分。
numpy.ediff1d(ary, to_end, to_begin)：数组的连续元素之间的差异。
numpy.gradient(f)：返回 N 维数组的梯度。
numpy.cross(a, b, axisa, axisb, axisc, axis)：返回两个(数组）向量的叉积。
numpy.trapz(y, x, dx, axis)：使用复合梯形规则沿给定轴积分。
'''
import numpy as np
a=np.arange(5)
a
array([0, 1, 2, 3, 4])

np.prod(a) # 所有元素乘积
0

np.sum(a) # 所有元素和
10

np.nanprod(a) # 默认轴上所有元素乘积
0

np.nansum(a) # 默认轴上所有元素和
10

np.cumprod(a) # 默认轴上元素的累积乘积。
array([0, 0, 0, 0, 0])

np.diff(a) # 默认轴上元素差分。
array([1, 1, 1, 1])


'''
如果你需要进行指数或者对数求解，可以用到以下这些方法。

numpy.exp(x)：计算输入数组中所有元素的指数。
numpy.expm1(x)：对数组中的所有元素计算 exp(x） - 1.
numpy.exp2(x)：对于输入数组中的所有 p, 计算 2 ** p。
numpy.log(x)：计算自然对数。
numpy.log10(x)：计算常用对数。
numpy.log2(x)：计算二进制对数。
numpy.log1p(x)：log(1 + x)。
numpy.logaddexp(x1, x2)：log2(2**x1 + 2**x2)。
numpy.logaddexp2(x1, x2)：log(exp(x1) + exp(x2))。
'''


'''
当然，numpy 也提供了一些用于算术运算的方法，使用起来会比 python 提供的运算符灵活一些，主要是可以直接针对数组。

numpy.add(x1, x2)：对应元素相加。
numpy.reciprocal(x)：求倒数 1/x。
numpy.negative(x)：求对应负数。
numpy.multiply(x1, x2)：求解乘法。
numpy.divide(x1, x2)：相除 x1/x2。
numpy.power(x1, x2)：类似于 x1^x2。
numpy.subtract(x1, x2)：减法。
numpy.fmod(x1, x2)：返回除法的元素余项。
numpy.mod(x1, x2)：返回余项。
numpy.modf(x1)：返回数组的小数和整数部分。
numpy.remainder(x1, x2)：返回除法余数。
'''
import numpy as np

a1 = np.random.randint(0, 10, 5)
a2 = np.random.randint(0, 10, 5)

a1
array([3, 7, 8, 0, 0])

a2
array([1, 8, 6, 4, 4])

np.add(a1, a2)
array([ 4, 15, 14,  4,  4])

np.reciprocal(a1)
array([0, 0, 0, , ])

np.negative(a1)
array([-3, -7, -8,  0,  0])

np.multiply(a1, a2)
array([ 3, 56, 48,  0,  0])

np.divide(a1, a2)
array([3, 0, 1, 0, 0])

np.power(a1, a2)
array([3,5764801,262144,0,0])

np.subtract(a1, a2)
array([ 2, -1,  2, -4, -4])

np.fmod(a1, a2)
array([0, 7, 2, 0, 0])

np.mod(a1, a2)
array([0, 7, 2, 0, 0])

np.modf(a1)
(array([ 0.,  0.,  0.,  0.,  0.]), array([ 3.,  7.,  8.,  0.,  0.]))

np.remainder(a1, a2)
array([0, 7, 2, 0, 0])



'''
求解向量、矩阵、张量的点积等同样是 numpy 非常强大的地方。

numpy.dot(a,b)：求解两个数组的点积。
numpy.vdot(a,b)：求解两个向量的点积。
numpy.inner(a,b)：求解两个数组的内积。
numpy.outer(a,b)：求解两个向量的外积。
numpy.matmul(a,b)：求解两个数组的矩阵乘积。
numpy.tensordot(a,b)：求解张量点积。
numpy.kron(a,b)：计算 Kronecker 乘积。
'''

'''
除了上面这些归好类别的方法，numpy 中还有一些用于数学运算的方法，归纳如下：

numpy.angle(z, deg)：返回复参数的角度。
numpy.real(val)：返回数组元素的实部。
numpy.imag(val)：返回数组元素的虚部。
numpy.conj(x)：按元素方式返回共轭复数。
numpy.convolve(a, v, mode)：返回线性卷积。
numpy.sqrt(x)：平方根。
numpy.cbrt(x)：立方根。
numpy.square(x)：平方。
numpy.absolute(x)：绝对值, 可求解复数。
numpy.fabs(x)：绝对值。
numpy.sign(x)：符号函数。
numpy.maximum(x1, x2)：最大值。
numpy.minimum(x1, x2)：最小值。
numpy.nan_to_num(x)：用 0 替换 NaN。
numpy.interp(x, xp, fp, left, right, period)：线性插值。
'''

'''
numpy 中还包含一些代数运算的方法，尤其是涉及到矩阵的计算方法，求解特征值、特征向量、逆矩阵等，非常方便。

numpy.linalg.cholesky(a)：Cholesky 分解。
numpy.linalg.qr(a ,mode)：计算矩阵的 QR 因式分解。
numpy.linalg.svd(a ,full_matrices,compute_uv)：奇异值分解。
numpy.linalg.eig(a)：计算正方形数组的特征值和右特征向量。
numpy.linalg.eigh(a, UPLO)：返回 Hermitian 或对称矩阵的特征值和特征向量。
numpy.linalg.eigvals(a)：计算矩阵的特征值。
numpy.linalg.eigvalsh(a, UPLO)：计算 Hermitian 或真实对称矩阵的特征值。
numpy.linalg.norm(x ,ord,axis,keepdims)：计算矩阵或向量范数。
numpy.linalg.cond(x ,p)：计算矩阵的条件数。
numpy.linalg.det(a)：计算数组的行列式。
numpy.linalg.matrix_rank(M ,tol)：使用奇异值分解方法返回秩。
numpy.linalg.slogdet(a)：计算数组的行列式的符号和自然对数。
numpy.trace(a ,offset,axis1,axis2,dtype,out)：沿数组的对角线返回总和。
numpy.linalg.solve(a,b)：求解线性矩阵方程或线性标量方程组。
numpy.linalg.tensorsolve(a,b ,axes)：为 x 解出张量方程a x = b
numpy.linalg.lstsq(a,b ,rcond)：将最小二乘解返回到线性矩阵方程。
numpy.linalg.inv(a)：计算逆矩阵。
numpy.linalg.pinv(a ,rcond)：计算矩阵的（Moore-Penrose）伪逆。
numpy.linalg.tensorinv(a ,ind)：计算N维数组的逆。
'''