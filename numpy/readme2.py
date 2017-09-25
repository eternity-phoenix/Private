'''
reshape �����ڲ��ı��������ݵ�ͬʱ���ı��������״�����У�numpy.reshape() ��Ч�� ndarray.reshape()��reshape �����ǳ��򵥣�
numpy.reshape(a, newshape)
���У�a ��ʾԭ���飬newshape ����ָ���µ���״(��������Ԫ��)��
'''

'''
ravel ��Ŀ���ǽ�������״�������ƽ������Ϊ 1 ά���顣ravel �������£�

numpy.ravel(a, order='C')
���У�a ��ʾ��Ҫ��������顣order ��ʾ�任ʱ�Ķ�ȡ˳��Ĭ���ǰ��������ζ�ȡ���� order='F' ʱ�����԰������ζ�ȡ����
'''

'''
moveaxis ���Խ���������ƶ����µ�λ�á��䷽�����£�

numpy.moveaxis(a, source, destination)
���У�

a�����顣
source��Ҫ�ƶ������ԭʼλ�á�
destination��Ҫ�ƶ������Ŀ��λ�á�

�����û�п�������ʲô��˼����������ƶ���֮��������ߵ� shape���ԶԱ�һ�¾������ˣ�
'''

'''
�� moveaxis ��ͬ���ǣ�swapaxes ������������������ᡣ�䷽�����£�

numpy.swapaxes(a, axis1, axis2)
���У�

a�����顣
axis1����Ҫ�������� 1 λ�á�
axis2����Ҫ���� 1 ����λ�õ��� 1 λ�á�

ͬ���������ǰ�������shape�Ա�һ��
'''

'''
transpose �����ھ����ת�ã������Խ� 2 ά����ĺ�������ύ�����䷽�����£�

numpy.transpose(a, axes=None)
���У�

a�����顣
axis����ֵĬ��Ϊ none����ʾת�á������ֵ����ô����ֵ�滻�ᡣ
'''

'''
atleast_xd ֧�ֽ���������ֱ����Ϊ xά������� x ���Ա�ʾ��1��2��3�������ֱ�ά��

numpy.atleast_1d()
numpy.atleast_2d()
numpy.atleast_3d()
'''

'''
�� numpy �У�����һϵ���� as ��ͷ�ķ��������ǿ��Խ��ض�����ת��Ϊ���飬��ɽ�����ת��Ϊ���󡢱�����ndarray �ȡ����£�

asarray(a��dtype��order)�����ض�����ת��Ϊ���顣
asanyarray(a��dtype��order)�����ض�����ת��Ϊ ndarray��
asmatrix(data��dtype)�����ض�����ת��Ϊ����
asfarray(a��dtype)�����ض�����ת��Ϊ float ���͵����顣
asarray_chkfinite(a��dtype��order)�����ض�����ת��Ϊ���飬��� NaN �� infs��
asscalar(a)������СΪ 1 ������ת��Ϊ������
������ asmatrix(data��dtype) ����������
'''
import numpy as np

a = np.arange(4).reshape(2,2)
np.asmatrix(a)

'''
concatenate ���Խ����������ָ����������һ���䷽��Ϊ��

numpy.concatenate((a1, a2, ...), axis=0)
���У�

(a1, a2, ...)����Ҫ���ӵ����顣
axis��ָ�������ᡣ
�ٸ����ӣ�
'''
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 10]])
c = np.array([[11, 12]])

np.concatenate((a, b, c), axis=0)


'''
�� numpy �У�����һϵ���� as ��ͷ�ķ��������ǿ��Խ��ض�����ת��Ϊ���飬��ɽ�����ת��Ϊ���󡢱�����ndarray �ȡ����£�

stack(arrays��axis)����������������������С�
column_stack()���� 1 ά������Ϊ�жѵ��� 2 ά�����С�
hstack()����ˮƽ����ѵ����顣
vstack()������ֱ����ѵ����顣
dstack()������ȷ���ѵ����顣
������ stack(arrays��axis) ����������
'''
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.stack((a, b))

# ��Ȼ��Ҳ���Ժ��Ŷѵ���

np.stack((a, b), axis=-1)

'''
split ����֮���Ƶ�һϵ�з�����Ҫ����������Ĳ�֣��о����£�

split(ary��indices_or_sections��axis)����������Ϊ��������顣
dsplit(ary��indices_or_sections)������ȷ��������ֳɶ�������顣
hsplit(ary��indices_or_sections)����ˮƽ���������ֳɶ�������顣
vsplit(ary��indices_or_sections)������ֱ���������ֳɶ�������顣
���棬���ǿ�һ�� split ������ʲôЧ����
'''
import numpy as np

a = np.arange(10)
np.split(a, 5)

# ���� 1 ά���飬����ά��Ҳ�ǿ���ֱ�Ӳ�ֵġ����磬���ǿ��Խ���������鰴�в��Ϊ 2��

import numpy as np

a = np.arange(10).reshape(2,5)
np.split(a, 2)


'''
delete(arr��obj��axis)�����ض���ɾ�������е������顣
���棬���ζ� 4 �ַ�������ʾ���������� delete ɾ����
'''
import numpy as np

a = np.arange(12).reshape(3,4)
np.delete(a, 2, 1)
# ����������ź��ᣬ���� 3 ��(���� 2)ɾ����

'''
insert(arr��obj��values��axis)�������������ض���֮ǰ����ֵ��
�ٿ�һ�� insert����, �÷��� delete �����ƣ�ֻ����Ҫ�ڵ���������λ��������Ҫ������������
'''

import numpy as np

a = np.arange(12).reshape(3,4)
b = np.arange(4)

np.insert(a, 2, b, 0)


'''
append(arr��values��axis)����ֵ���ӵ������ĩβ�������� 1 ά���顣
append ���÷�Ҳ�ǳ��򵥡�ֻ��Ҫ���ú���Ҫ���ӵ�ֵ����λ�þͺ��ˡ�����ʵ�൱��ֻ����ĩβ����� insert����������һ��ָ�������Ĳ�����
'''
import numpy as np

a = np.arange(6).reshape(2,3)
b = np.arange(3)

np.append(a, b)
# ע�� append��������ֵ��Ĭ����չƽ״̬�µ� 1 ά���顣

'''
resize(a��new_shape)��������ߴ���������趨��
resize �ͺܺ�����ˣ�ֱ�Ӿ����Ӱɣ�
'''
import numpy as np

a = np.arange(10)
a.resize(2,5)
'''
��� resize ������������� reshape һ���أ����Ǹı�����ԭ�е���״��

��ʵ������ֱ����������ģ��������ڶ�ԭ�����Ӱ�졣reshape �ڸı���״ʱ������Ӱ��ԭ���飬�൱�ڶ�ԭ��������һ�ݿ������� resize ���Ƕ�ԭ����ִ�в�����
'''

'''
�� numpy �У����ǻ����Զ�������з�ת������

fliplr(m)�����ҷ�ת���顣
flipud(m)�����·�ת���顣
�ٸ����ӣ�
'''
import numpy as np

a = np.arange(16).reshape(4,4)
n.fliplr(a)
n.flipud(a)


'''
numpy.random.rand(d0, d1, ..., dn) ����������Ϊ��ָ��һ�����飬��ʹ�� [0, 1) �������������䣬��Щ���ݾ��ȷֲ���
'''
import numpy as np

np.random.rand(2,5)
'''
numpy.random.randn(d0, d1, ..., dn) �� numpy.random.rand(d0, d1, ..., dn) ���������ڣ����ص�������ݷ��ϱ�׼��̫�ֲ���

numpy.random.randint(low, high, size, dtype) ������������ [low, high) �����������ע������һ���뿪������䡣

numpy.random.random_integers(low, high, size) ������������ [low, high] �� np.int �������������ע������һ�������䡣

numpy.random.random_sample(size) ���������� [0, 1) ����������ָ�� size �������������
�� numpy.random.random_sample ���Ƶķ������У�
numpy.random.random([size])
numpy.random.ranf([size])
numpy.random.sample([size])
���� 4 ����Ч������ࡣ

'''

'''
numpy.random.choice(a, size, replace, p) ������������� 1 ά�����������������
'''
import numpy as np

np.random.choice(10,5)
# ����Ĵ��뽫���� np.arange(10) ������ 5 ���������



'''
����������ܵ� 6 ����������ɷ�����numpy ���ṩ�˴����������ض������ܶȷֲ����������ɷ��������ǵ�ʹ�÷���������ǳ����ƣ�����Ͳ���һһ�����ˡ��о����£�

numpy.random.beta(a��b��size)���� Beta �ֲ��������������
numpy.random.binomial(n, p, size)���Ӷ���ֲ��������������
numpy.random.chisquare(df��size)���ӿ����ֲ��������������
numpy.random.dirichlet(alpha��size)���� Dirichlet �ֲ��������������
numpy.random.exponential(scale��size)����ָ���ֲ��������������
numpy.random.f(dfnum��dfden��size)���� F �ֲ��������������
numpy.random.gamma(shape��scale��size)���� Gamma �ֲ��������������
numpy.random.geometric(p��size)���Ӽ��ηֲ��������������
numpy.random.gumbel(loc��scale��size)���� Gumbel �ֲ��������������
numpy.random.hypergeometric(ngood, nbad, nsample, size)���ӳ����ηֲ��������������
numpy.random.laplace(loc��scale��size)����������˹˫ָ���ֲ��������������
numpy.random.logistic(loc��scale��size)�����߼��ֲ��������������
numpy.random.lognormal(mean��sigma��size)���Ӷ�����̬�ֲ��������������
numpy.random.logseries(p��size)���Ӷ���ϵ�зֲ��������������
numpy.random.multinomial(n��pvals��size)���Ӷ���ֲ��������������
numpy.random.multivariate_normal(mean, cov, size)���Ӷ������̬�ֲ��������������
numpy.random.negative_binomial(n, p, size)���Ӹ�����ֲ��������������
numpy.random.noncentral_chisquare(df��nonc��size)���ӷ����Ŀ����ֲ��������������
numpy.random.noncentral_f(dfnum, dfden, nonc, size)���ӷ����� F �ֲ��г�ȡ������
numpy.random.normal(loc��scale��size)������̬�ֲ��������������
numpy.random.pareto(a��size)���Ӿ���ָ����״�� Pareto II �� Lomax �ֲ��������������
numpy.random.poisson(lam��size)���Ӳ��ɷֲ��������������
numpy.random.power(a��size)���Ӿ�����ָ�� a-1 �Ĺ��ʷֲ����� 0��1 �������������
numpy.random.rayleigh(scale��size)���������ֲ��������������
numpy.random.standard_cauchy(size)���ӱ�׼ Cauchy �ֲ��������������
numpy.random.standard_exponential(size)���ӱ�׼ָ���ֲ��������������
numpy.random.standard_gamma(shape��size)���ӱ�׼ Gamma �ֲ��������������
numpy.random.standard_normal(size)���ӱ�׼��̬�ֲ��������������
numpy.random.standard_t(df��size)���Ӿ��� df ���ɶȵı�׼ѧ�� t �ֲ��������������
numpy.random.triangular(left��mode��right��size)�������Ƿֲ��������������
numpy.random.uniform(low��high��size)���Ӿ��ȷֲ��������������
numpy.random.vonmises(mu��kappa��size)���� von Mises �ֲ��������������
numpy.random.wald(mean��scale��size)���� Wald �򷴸�˹�ֲ��������������
numpy.random.weibull(a��size)�����������ֲ��������������
numpy.random.zipf(a��size)���� Zipf �ֲ��������������
'''