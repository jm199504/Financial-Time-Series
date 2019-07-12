**使用CNN模型预测未来一天的股价涨跌**

**数据介绍**

open 开盘价；close 收盘价；high 最高价

low 最低价；volume 交易量；label 涨/跌

**训练规模**

特征数量×5；天数×5 = 5 × 5

**卷积过程**

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Prediction-CNN/images/conv.gif" width = "500" />

**最大池化过程**

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Prediction-CNN/images/pool.png" width = "500" />

**代码流程**

1. 获取股票数据
2. 数据归一化
3. 数据预处理（划分成5×5）
4. 数据集分割（训练集和测试集）
5. 定义卷积神经网络
6. 评估预测模型

**模型架构**

<img src="<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Prediction-CNN/images/model.png" width = "500" />">
