'''
神经网络设计脚本的功能就是决定神经网络使用的隐藏节点的数量，这里我们从5个节点开始增长，每次增加5个，到50个为止，打印性能进行比较
'''

import numpy as np
from ocr import OCRNeuralNetwork
from sklearn.cross_validation import train_test_split

def test(data_matrix, data_labels, test_indices, nn):
    correct_guess_count = 0
    for i in test_indices:
        test = data_matrix[i]
        prediction = nn.predict(test)
        if data_labels[i] == prediction:
            correct_guess_count += 1
    return correct_guess_count / len(test_indices)

data_matrix = np.loadtxt('data.csv', delimiter=',').tolist()
data_labels = np.loadtxt('dataLabels.csv').tolist()

# create training and test sets.
train_indices, test_indices = train_test_split(list(range(5000)))

for i in range(5, 50, 5):
    nn = OCRNeuralNetwork(i, data_matrix, data_labels, train_indices, False)
    performance = str(test(data_matrix, data_labels, test_indices, nn))
    print("{i} Hidden Nodes: {val}".format(i=i, val=performance))


'''
运行脚本查看结果

通过输出我们判断15个隐藏节点可能是最优的。从10到15增加了1％的精确度，之后需要再增加20个节点才能有如此的增长，但同时也会大大地增加了计算量，因此15个节点性价比最高。当然不追求性价比电脑性能也够用的话还是选择准确度最高的节点数为好。
'''
