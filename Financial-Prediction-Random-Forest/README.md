**基于随机森林预测股票未来第d+k天相比于第d天的涨/跌（简易版）**

参考论文：Predicting the direction of stock market prices using random forest 

**论文流程：**

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Prediction-Random-Forest/images/model.png" width="300">

**算法流程：**

获取金融数据->指数平滑->计算技术指标->数据归一化->随机森林模型预测

**函数介绍：**

1、get_stock_data 通过Tushare获取原始股票数据 

2、exponential_smoothing、em_stock_data 股票指数平滑处理 

3、calc_technical_indicators 计算常用的技术指标 

4、normalization 数据归一化处理并分割数据集 

5、random_forest_model 随机森林模型并返回准确率和特征排名

**决策树：**

（1）ID3: 基于信息增益大的数据特征划分层次

（2）C4.5: 基于信息增益比=信息增益/特征熵划分层次

（3）CART: 基于Gini划分层次

基于Bagging集成学习算法，有多棵决策树组成（通常是CART决策树），其主要特性有：

（1）样本和特征随机采样

（2）适用于数据维度大的数据集

（3）对异常样本点不敏感

（4）可以并行训练（决策树间独立同分布）

**算法输出：**

注意：算法仅用于参考学习交流，由于是研一时期独立编写（以后可能进一步完善），所公开的代码并非足够完善和严谨，如以下问题：

1. 模型涉及参数未寻优（可考虑网格搜索、随机搜索、贝叶斯优化）

   1. 指数平滑因子
   
   2. 随机森林模型树数量、决策树深度、叶子节点最小样本数等
   
   3. 未来第k天的选择
   
   4. 归一化方法
   
2. 随机森林模型其实本身不需要数据归一化（如算法对数据集进行归一化也需要考虑对训练集、验证集、测试集独立归一化）

3. 股票预测考虑的数据特征：

   1. 原始数据特征（open/close/high/low）
   
   2. 技术指标（Technical indicator）
   
   3. 企业公开公告信息
   
   4. 企业未来规划
   
   5. 企业年度报表
   
   6. 社会舆论
   
   7. 股民情绪
   
   8. 国家政策
   
   9. 股票间影响等
   
4.模型输出结果

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Prediction-Random-Forest/images/result.png">

5.随机森林参数优化参考表

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Prediction-Random-Forest/images/param.png">
