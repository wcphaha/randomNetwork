import random
import time
import csv
import codecs
import pygame

Title = '随机网络生成过程'
Width = 800
Height = 600
P = 0.2
N = 25
# 线条颜色
Black = (0, 0, 0)
white = (255, 255, 255)
Red = (255, 0, 0)
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
            time.sleep(0.1)
            i[0].update_degree()
            i[1].update_degree()
            pygame.draw.line(screen, Red, i[0].position, i[1].position, 1)
            pygame.display.update()


def data_write_csv(file_name, datas):  # file_name为写入CSV文件的路径，datas为要写入数据列表
    file_csv = codecs.open(file_name, 'w+', 'utf-8')  # 追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in datas:
        writer.writerow(str(data))
    print("保存文件成功，处理结束")
