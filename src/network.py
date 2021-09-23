import itertools
from sys import *
from pygame.locals import *
import pygame
from src.constant import *
import random
import numpy as np


class Network:
    def __init__(self):
        self.title = Title
        self.width = Width
        self.height = Height
        self.screen = None
        self.N = N
        self.P = P
        self.Matrix = []
        self.Nodes = {}
        self.seq = []
        self.init_pygame()
        self.init_nodes()
        self.export_datas()
        self.update()

    def init_nodes(self):
        # 随机初始化所有节点的位置
        for i in range(self.N):
            pos = [random.randint(50, self.width - 50), random.randint(50, self.height - 50)]
            self.Nodes[i] = Node(pos, i)
            self.seq.append(i)
            pygame.draw.circle(self.screen, Green, pos, Node_size)
            # time.sleep(0.1)
            pygame.display.update()
        # 根据模型初始化连边
        res = []
        # 初始化匹配
        res = list(itertools.combinations(self.seq, 2))
        # 利用匹配数组，初始化边
        m = init_arc(self.screen, res, self.Nodes)
        self.export_adjMatrix(m)
        # 为了便于观察，将所有节点重新绘制一遍
        for node in self.Nodes.values():
            pygame.draw.circle(self.screen, Green, node.position, Node_size)
            # time.sleep(0.1)
            pygame.display.update()

    def export_datas(self):
        datas = self.export_degrees()
        data_write_csv(degree_datapath, datas)
        sum = 0
        for i in range(len(datas[0])):
            sum += datas[0][i] * datas[1][i]
        print('平均度：', sum / N)

    def init_pygame(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.screen.fill(white)

    def update(self):
        while True:
            self.event_handler()
            pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    # 当按下D键时，输出一下所有节点的度
                    degrees = []
                    for i in self.Nodes.values():
                        degrees.append(i.degree)
                    # degrees.sort(reverse=True)
                    print(degrees)
                if event.key == K_m:
                    # 当按下M键时，输出邻接矩阵
                    print(self.Matrix)

    def export_degrees(self):
        res = []
        for i in self.Nodes.values():
            res.append(i.degree)
        data = [[], []]
        for i in range(int(2 * N * P)):
            if i in res:
                data[0].append(i)
                data[1].append(res.count(i))
        return data

    def export_adjMatrix(self, m):
        matrix = np.zeros((N, N), dtype=int)
        for i in m:
            matrix[i[0].seq][i[1].seq] = 1
        self.Matrix = matrix + matrix.T
