#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import numpy as np
import random
from http.server import BaseHTTPRequestHandler, HTTPServer
from ocr import OCRNeuralNetwork


#服务器端配置
HOST_NAME = 'localhost'
PORT_NUMBER = 9000

# 这个值是通过运行神经网络设计脚本得到的最优值
HIDDEN_NODE_COUNT = 15

# 加载数据集
data_matrix = np.loadtxt('data.csv', delimiter=',')
data_labels = np.loadtxt('dataLabels.csv')

# 转换成list类型
data_matrix = data_matrix.tolist()
data_labels = data_labels.tolist()

# 数据集一共5000个数据，train_indice存储用来训练的数据的序号
train_indice = list(range(5000))

# 打乱训练顺序
random.shuffle(train_indice)

nn = OCRNeuralNetwork(HIDDEN_NODE_COUNT, data_matrix, data_labels, train_indice)

class JSONHandler(BaseHTTPRequestHandler):
    """处理接收到的POST请求"""
    def do_POST(self):
        response_code = 200
        response = ''
        var_len = int(self.headers.get('Content-Length'))
        #content = self.rfile.read(var_len)
        # payload = json.loads(content)
        payload = json.loads(self.rfile.read(var_len))

        # 如果是训练请求，训练然后保存训练完的神经网络
        if payload.get('train'):
            nn.train(payload['trainArray'])
            nn.save()
        # 如果是预测请求，返回预测值
        elif payload.get('predict'):
            print(nn.predict(data_matrix[0]))
            response = {
                'type': 'test',
                'result': nn.predict(payload['image'])
            }
        else:
            response_code = 400
        
        self.send_response(response_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        if response:
            self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_GET(self):
        if self.path == '/' or self.path.find('.') > 0:
            if self.path == '/':
                file = 'ocr.html'
            else:
                file =  self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            with open(file, 'rb') as f:
                self.wfile.write(f.read())
        else:
            response_code = 404


if __name__ == '__main__':
    server = HTTPServer((HOST_NAME, PORT_NUMBER), JSONHandler)
    print('server on ', server.server_address)

    server.serve_forever()

