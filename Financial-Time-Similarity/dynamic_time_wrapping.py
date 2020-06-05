from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import pandas as pd

# 计算股票间的对数收益时间序列间的动态时间规整距离

path1,path2 = "000001.XSHE.csv","000063.XSHE.csv",
feature = "rclose"
length = 20
window,psi = 10,5

rc1,rc2 = pd.read_csv(path1)[feature][:length],pd.read_csv(path2)[feature][:length]
dis, paths = dtw.warping_paths(rc1, rc2, window=window, psi=psi)

# 动态时间规整距离
print(dis)

# 绘图（输出形式）
best_path = dtw.best_path(paths)
dtwvis.plot_warpingpaths(rc1, rc2, paths, best_path,shownumbers=True)

# 绘图（保存）
path = dtw.warping_path(rc1, rc2)
dtwvis.plot_warping(rc1, rc2, path, filename="wrapping.png")