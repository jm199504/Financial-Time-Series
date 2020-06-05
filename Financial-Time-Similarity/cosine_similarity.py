import pandas as pd
import numpy as np
path1,path2 = "000001.XSHE.csv","000063.XSHE.csv",
feature = "rclose"
length = 20
rc1,rc2 = pd.read_csv(path1)[feature][:length],pd.read_csv(path2)[feature][:length]


cosine = np.dot(rc1, rc2) / (np.linalg.norm(rc1) * (np.linalg.norm(rc2)))

print(cosine)