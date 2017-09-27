'''
图像分割：利用图像的灰度、颜色、纹理、形状等特征，把图像分成若 干个互不重叠的区域，并使这些特征在同一区域内呈现相似性，在不同的区 域之间存在明显的差异性。然后就可以将分割的图像中具有独特性质的区域 提取出来用于不同的研究。
'''
import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans

def load_data(file_path):
    with open(file_path,'rb') as f: #二进制打开
        data = []
        img = image.open(f) #以列表形式返回图片像素值
        m,n = img.size #活的图片大小
        for i in range(m):
            for j in range(n):  #将每个像素点RGB颜色处理到0-1范围内并存放data
                x,y,z = img.getpixel((i,j))
                data.append([x/256.0,y/256.0,z/256.0])
        return np.mat(data),m,n #以矩阵型式返回data，图片大小


img_data,row,col = load_data('1.jpg')
label = KMeans(n_clusters=3).fit_predict(img_data)  #聚类中心的个数为3
label = label.reshape([row,col])    #聚类获得每个像素所属的类别
pic_new = image.new("L",(row,col))  #创建一张新的灰度图保存聚类后的结果
for i in range(row):    #根据所属类别向图片中添加灰度值
    for j in range(col):
        pic_new.putpixel((i,j),int(256/(label[i][j]+1)))

pic_new.show()