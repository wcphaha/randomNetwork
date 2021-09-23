import random
import time
import pandas as pd
import pygame

Title = '随机网络生成过程'
Width = 1000
Height = 700
P = 0.015
N = 100
Node_size = 8
# 线条颜色
Black = (0, 0, 0)
white = (255, 255, 255)
Red = (255, 0, 0)
Blue = (0, 0, 255)
GreenYellow = (173, 255, 47)
Green = (50, 205, 50)
Purple = (160, 32, 240)
degree_datapath = 'datas/Degree_info.txt'
adjMatrix_datapath = 'datas/Matrix.txt'


class Node:
    degree = 0

    def __init__(self, position, seq):
        self.position = position
        self.seq = seq

    def update_degree(self):
        self.degree += 1

    def __str__(self):
        return f'序号:{self.seq},度:{self.degree},位置:{self.position}'


def init_arc(screen, s, nodes):
    match = []
    for item in s:
        match.append([nodes[item[0]], nodes[item[1]]])
    m = []
    for i in match:
        rand_number = random.random()
        if rand_number < P:
            m.append(i[:])
            i[0].update_degree()
            i[1].update_degree()
            pygame.draw.line(screen, Purple, i[0].position, i[1].position, 1)
            # time.sleep(0.2)
            pygame.display.update()
    # 返回所有的连边
    return m


def data_write_csv(file_name, datas):
    a, b = datas[0], datas[1]
    dataframe = pd.DataFrame({'degree': a, 'count': b})
    dataframe.to_csv(file_name, index=False, sep=',', header=None)
    print("保存文件成功，处理结束")
