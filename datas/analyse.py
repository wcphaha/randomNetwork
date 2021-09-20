import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print(12312312312)
# 数据文件访问路径
data_path = './Network_info.txt'
# 以CSV格式读取数据信息
data = pd.read_csv(data_path, header=None, names=['degree', 'count'])
data.plot(kind='line', x='degree', y='count', figsize=(12, 8))
# 展示
plt.show()
