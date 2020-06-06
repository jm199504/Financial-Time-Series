import numpy as np

# 数据归一化
def normalization(method,data):
    if method == 'std':
        for i in range(len(data)):
            for j in range(data.shape[2]):
                data[i][:, j] = (data[i][:, j] - np.mean(data[i][:, j])) / (np.std(data[i][:, j], ddof=1) + 1e-10 )
        return data
    if method == 'maxmin':
        for i in range(len(data)):
            for j in range(data.shape[2]):
                data[i][:, j] = (data[i][:, j] - np.min(data[i][:, j])) / (np.max(data[i][:, j]) - np.min(data[i][:, j]) + 1e-10)
        return data