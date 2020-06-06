import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
df = pd.read_csv('000001.XSHE.csv')[:1000]
f, ax = plt.subplots(figsize=(14, 10))
featureslist = list(df.columns)

train_df = df[featureslist]
h = sns.heatmap(train_df.corr(), cmap='RdBu', linewidths=0.1, ax=ax,cbar=False,annot=True)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)

cb = h.figure.colorbar(h.collections[0])  # 显示colorbar
cb.ax.tick_params(labelsize=15)  # 设置colorbar刻度字体大小。

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
print(train_df.corr())
# 设置Axes的标题
ax.set_title('技术指标之间的相关性',fontsize=22)
plt.show()

