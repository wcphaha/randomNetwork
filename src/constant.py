import random
import time
import pandas as pd
import pygame

Title = '随机网络生成过程'
Width = 1000
Height = 700
P = 0.05
N = 101
Node_size = 8
# 线条颜色
Black = (0, 0, 0)
white = (255, 255, 255)
Red = (255, 0, 0)
Blue = (0, 0, 255)
GreenYellow = (173, 255, 47)
Green = (50, 205, 50)
Purple = (160, 32, 240)
Datapath = 'datas/Network_info.txt'


class Node:
    degree = 0

    def __init__(self, position, seq):
        self.position = position
        self.seq = seq

    def update_degree(self):
        self.degree += 1

    def __str__(self):
        return f'序号:{self.seq},度:{self.degree},位置:{self.position}'


def init_match(nums, res, n=2, track=[]):
    if 2 == len(track):
        t = list(track)
        t.sort()
        if t not in res:
            res.append(t)
            return
        else:
            return
    for i in nums:
        if i in track:
            continue
        track.append(i)
        init_match(res=res, nums=nums, track=track)
        track.pop()
    nums = nums[1:]


def init_arc(screen, s, nodes):
    match = []
    for i in nodes:
        for j in nodes:
            if [i.seq, j.seq] in s:
                match.append([i, j])
    for i in match:
        rand_number = random.random()
        if rand_number < P:
            i[0].update_degree()
            i[1].update_degree()
            pygame.draw.line(screen, Purple, i[0].position, i[1].position, 1)
            # time.sleep(0.2)
            pygame.display.update()


def data_write_csv(file_name, datas):
    a, b = datas[0], datas[1]
    dataframe = pd.DataFrame({'degree': a, 'count': b})
    dataframe.to_csv(file_name, index=False, sep=',', header=None)
    print("保存文件成功，处理结束")
