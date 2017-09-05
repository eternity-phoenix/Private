import json
import os
import math
import numpy as np
from collections import namedtuple

'''
如之前所说，我们使用反向传播算法（Backpropagation）来训练神经网络，算法背后的原理推导推荐阅读这篇博文：反向传播神经网络极简入门

算法主要分为三个步骤：

第一步：初始化神经网络

第二步：前向传播

第三步：反向传播
'''

class OCRNeuralNetwork(object):
    
    LEARNING_RATE = 0.1
    WIDTH_IN_PIXELS = 20
    # 保存文件的路径
    NN_FILE_PATH = 'nn.json'

    def __init__(self, num_hidden_nodes, data_matrix, data_labels, training_indices, use_file=True):
        # 使用numpy的vectorize能得到标量函数的向量化版本，这样就能直接处理向量了：        
        # sigmoid函数
        self.sigmoid = np.vectorize(self._sigmoid_scalar) 

        # sigmoid求导函数
        self.sigmoid_prime = np.vectorize(self._sigmoid_prime_scalar)

        # 决定了要不要导入nn.json
        self._use_file = use_file
        # 数据集
        self.data_matrix = data_matrix
        self.data_labels = data_labels

        # 初始化权值矩阵与偏置向量：
        '''
        这里说明一下会用到的每一个矩阵/向量及其形状：

        变量名	            描述	                形状
        y0	                输入层	                1 * 400
        theta1	            输入-隐藏层权值矩阵	    隐藏层节点数 * 400
        input_layer_bias	输入-隐藏层偏置向量	    隐藏层节点数 * 1
        y1	                隐藏层	                隐藏层节点数 * 1
        theta2	            隐藏-输出层权值矩阵	    10 * 隐藏层节点数
        hidden_layer_bias	隐藏-输出层偏置向量	    10 * 1
        y2	                输出层	                10 * 1
        '''
        if (not os.path.isfile(OCRNeuralNetwork.NN_FILE_PATH) or not use_file):
            # 初始化神经网络
            self.theta1 = self._rand_initialize_weights(400, num_hidden_nodes)
            self.theta2 = self._rand_initialize_weights(num_hidden_nodes, 10)
            self.input_layer_bias = self._rand_initialize_weights(1, num_hidden_nodes)
            self.hidden_layer_bias = self._rand_initialize_weights(1, 10)

            # 训练并保存
            TrainData = namedtuple('TrainData', ['y0', 'label'])
            self.train([TrainData(self.data_matrix[i], int(self.data_labels[i])) for i in training_indices])
            self.save()
        else:
            # 如果nn.json存在则加载
            self._load()
        

    def _rand_initialize_weights(self, size_in, size_out):
        '''
        第一步：初始化神经网络
        一般将所有权值与偏置量置为(-1,1)范围内的随机数，在我们这个例子中，使用(-0.06,0.06)这个范围，输入层到隐藏层的权值存储在矩阵theta1中，
        偏置量存在input_layer_bias中，隐藏层到输出层则分别存在theta2与hidden_layer_bias中。

        创建随机矩阵的代码如下，注意输出的矩阵是以size_out为行，size_in为列。可能你会想为什么不是size_in在左边。
        你可以这么想，一般都是待处理的输入放在右边，处理操作（矩阵）放在左边。(矩阵乘法)
        '''
        return [x * 0.12 - 0.06 for x in np.random.rand(size_out, size_in)]

    def _sigmoid_scalar(self, z):
        '''
        第二步：前向传播

        前向传播就是输入数据通过一层一层计算到达输出层得到输出结果，输出层会有10个节点分别代表0~9，
        哪一个节点的输出值最大就作为我们的预测结果。还记得前面说的激发函数吗？
        一般用sigmoid函数作为激发函数。
        函数图形可以参考    sigmoid函数.png

        可以将实数范围的数字映射到(0, 1)，S型的形状也很理想，最关键是导数可直接得到。
        '''
        return 1 / (1 + math.e ** -z) 


    def _sigmoid_prime_scalar(self, z):
        '''
        sigmoid_prime的作用就是先sigmoid再求导数。
        '''
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    def train(self, training_data_array):
        for data in training_data_array:
            # 前向传播得到结果向量
            y1 = np.dot(np.mat(self.theta1), np.mat(data['y0']).T)
            sum1 =  y1 + np.mat(self.input_layer_bias)
            y1 = self.sigmoid(sum1)

            y2 = np.dot(np.array(self.theta2), y1)
            y2 = np.add(y2, self.hidden_layer_bias)
            y2 = self.sigmoid(y2)

            '''
            第三步：反向传播
            第三步是训练的关键，它需要通过计算误差率然后系统根据误差改变网络的权值矩阵和偏置向量。
            通过训练数据的标签我们得到actual_vals用来和输出层相减得到误差率output_errors，
            输出层的误差只能用来改进上一层，想要改进上上一层就需要计算上一层的输出误差，
            '''
            # 后向传播得到误差向量
            actual_vals = [0] * 10 
            actual_vals[data['label']] = 1
            output_errors = np.mat(actual_vals).T - np.mat(y2)
            hidden_errors = np.multiply(np.dot(np.mat(self.theta2).T, output_errors), self.sigmoid_prime(sum1))

            # 更新权重矩阵与偏置向量
            '''
            LEARNING_RATE是学习步进，这里我们设置成0.1，步子大虽然学得快，但也容易扭到，步子小得到的结果会更精准。
            '''
            self.theta1 += self.LEARNING_RATE * np.dot(np.mat(hidden_errors), np.mat(data.y0))
            self.theta2 += self.LEARNING_RATE * np.dot(np.mat(output_errors), np.mat(y1).T)
            self.hidden_layer_bias += self.LEARNING_RATE * output_errors
            self.input_layer_bias += self.LEARNING_RATE * hidden_errors

    def predict(self, test):
        '''
        预测的代码就相当于前向传播：
        '''
        y1 = np.dot(np.mat(self.theta1), np.mat(test).T)
        y1 =  y1 + np.mat(self.input_layer_bias) # Add the bias
        y1 = self.sigmoid(y1)

        y2 = np.dot(np.array(self.theta2), y1)
        y2 = np.add(y2, self.hidden_layer_bias) # Add the bias
        y2 = self.sigmoid(y2)

        results = y2.T.tolist()[0]
        return results.index(max(results))

    def save(self):
        if not self._use_file:
            return

        json_neural_network = {
            "theta1":[np_mat.tolist()[0] for np_mat in self.theta1],
            "theta2":[np_mat.tolist()[0] for np_mat in self.theta2],
            "b1":self.input_layer_bias[0].tolist()[0],
            "b2":self.hidden_layer_bias[0].tolist()[0]
        };
        with open(OCRNeuralNetwork.NN_FILE_PATH,'w', encoding='utf-8') as nnFile:
            json.dump(json_neural_network, nnFile)

    def _load(self):
        if not self._use_file:
            return

        with open(OCRNeuralNetwork.NN_FILE_PATH, 'r', encoding='utf-8') as nnFile:
            nn = json.load(nnFile)
        self.theta1 = [np.array(li) for li in nn['theta1']]
        self.theta2 = [np.array(li) for li in nn['theta2']]
        self.input_layer_bias = [np.array(nn['b1'][0])]
        self.hidden_layer_bias = [np.array(nn['b2'][0])]

