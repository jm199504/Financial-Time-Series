import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
length = 20
stock1 = pd.read_csv('../data/000001.XSHE.csv').close[:length]
stock2 = pd.read_csv('../data/000063.XSHE.csv').close[:length]
plt.figure()
ax = plt.subplot(2,1,1)
plt.plot(np.arange(len(stock1)),list(stock1),color='blue',label='股票1')
plt.scatter(np.arange(len(stock1)),list(stock1),color='blue')
plt.legend()
plt.title('时间窗口内收盘价时间序列')
ax = plt.subplot(2,1,2)
plt.plot(np.arange(len(stock2)),list(stock2),color='orange',label='股票2')
plt.scatter(np.arange(len(stock2)),list(stock2),color='orange')
plt.legend()
plt.show()
