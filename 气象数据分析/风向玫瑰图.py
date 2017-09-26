import numpy as np
import pandas as pd

df_ravenna = pd.read_csv('WeatherData/ravenna_270615.csv')

import matplotlib

matplotlib.use('TKAgg')

import matplotlib.pyplot as plt

# 绘制极区图的坐标系
# fig, ax = plt.subplots([0.025, 0.025, 0.95, 0.95], projection='polar')
ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)

hist, bins = np.histogram(df_ravenna['wind_deg'],8,[0,360])

'''
要表示呈360度分布的数据点，最好使用另一种可视化方法：极区图。

首先，创建一个直方图，也就是将360度分为八个面元，每个面元为45度，把所有的数据点分到这八个面元中。

hist, bins = np.histogram(df_ravenna['wind_deg'],8,[0,360])
print hist
print bins
histogram()函数返回结果中的数组hist为落在每个面元的数据点数量。
[ 0 5 11 1 0 1 0 0]

返回结果中的数组bins定义了360度范围内各面元的边界。

[ 0. 45. 90. 135. 180. 225. 270. 315. 360.]
'''

def showRoseWind(values,city_name,max_value):
    '''
    showRoseWind()，它有三个参数：values数组，指的是想为其作图的数据，也就是这里的hist数组；第二个参数city_name为字符串类型，指定图表标题所用的城市名称；最后一个参数max_value为整型，指定最大的蓝色值。
    '''
    N = 8

    # theta = [pi*1/4, pi*2/4, pi*3/4, ..., pi*2]
    theta = np.arange(0.,2 * np.pi, 2 * np.pi / N) + 2 * np.pi / N / 2
    radii = np.array(values)

    # 列表中包含的是每一个扇区的 rgb 值，x越大，对应的color越接近蓝色
    colors = [(1-x/max_value, 1-x/max_value, 0.75) for x in radii]

    # 画出每个扇区
    ax.bar(theta, radii, width=(2*np.pi/N), bottom=0.0, color=colors)

    # 设置极区图的标题
    ax.set_title(city_name, x=0.2, fontsize=20)

showRoseWind(hist, 'Ravenna', max(hist))
plt.show()


# 定义RoseWind_Speed函数，计算将360度范围划分成的八个面元中每个面元的平均风速。

def RoseWind_Speed(df_city):
    # degs = [45, 90, ..., 360]
    degs = np.arange(45,361,45)
    tmp = []
    for deg in degs:
        # 获取 wind_deg 在指定范围的风速平均值数据
        tmp.append(df_city[(df_city['wind_deg']>(deg-46)) & (df_city['wind_deg']<deg)]
        ['wind_speed'].mean())
    return np.array(tmp)

showRoseWind(RoseWind_Speed(df_ravenna),'Ravenna',max(hist))
plt.show()



