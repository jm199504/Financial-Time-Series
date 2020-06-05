import os
import pandas as pd
from scipy.stats import pearsonr

# 计算股票间的对数收益时间序列间的皮尔逊相关系数

path1,path2 = "000001.XSHE.csv","000063.XSHE.csv",
feature = "rclose"
length = 20

rc1,rc2 = pd.read_csv(path1)[feature][:length],pd.read_csv(path2)[feature][:length]
pcc = pearsonr(rc1,rc2)[0]

# 皮尔逊相关系数
print(pcc)
