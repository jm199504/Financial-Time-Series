### 金融时间序列（数据预测 / 相似度 / 数据处理）

![author](https://img.shields.io/static/v1?label=Author&message=junmingguo&color=green)
![language](https://img.shields.io/static/v1?label=Language&message=python3&color=orange) ![topics](https://img.shields.io/static/v1?label=Topics&message=financial-time-series&color=blue)


#### 1. Financial-Prediction-Methods（金融时间序列预测方法）

- 1.1 Financial-Prediction-CNN（卷积神经网络）

- 1.2 Financial-Prediction-LSTM（长短期记忆神经网络）

- 1.3 Financial-Prediction-Random-Forest（随机森林）

- 1.4 Financial-Prediction-ARMA（自回归滑动平均模型）

- 1.5 Financial-Prediction-ARIMA（自回归积分移动平均模型）

- 1.6 Financial-Prediction-Muiti-Input-Conv1D（多输入Conv1D模型）

- 1.7 Financial-Prediction-2DCNN（2D卷积神经网络）

- 1.8 Financial-Prediction-3DCNN（3D卷积神经网络）

---

#### 2. Financial-Time-Similarity（金融时间序列相似度计算）

- 2.1 pearson_correlation_coefficient（皮尔逊相关系数）

- 2.2 dynamic_time_wrapping（动态时间规整）

- 2.3 cosine similarity（余弦相似度）

- 2.4 similarity_time_series.py（相似金融时间序列绘制）

---

#### 3. Finance-Time-Others（金融时间序列其他处理）

- 3.1 calc_variance.py（计算特征方差）
- 3.2 confuse_matrix.py（绘制混淆矩阵）

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Others/images/matrix.png" width = "500" />

- 3.3 corr.py（特征间相关性）

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Others/images/corr.png" width = "500" />

- 3.4 result_bar.py（绘制预测模型性能——柱状图）

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Others/images/bar.png" width = "700" />

- 3.5 result_plot.py（绘制预测模型性能——折线图）

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Others/images/plot.png" width = "500" />

- 3.6 evaluation.py（计算分类的评价指标）

  - 准确率Accuracy

  - 精确率Precision
  - 召回率Recall
  - 特异度Specificity
  - 综合评价指标F-measure
  - 马修斯相关系数MCC(Matthews Correlation Coefficient)
- 3.7 normalization.py（窗口数据归一化）
  - z-score标准化（std）
  - 最大最小归一化（maxmin）
- 3. 8roc.py（roc曲线绘制）

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Others/images/roc.png" width = "500" />

- 3.9 confusion_matrix.py（混淆矩阵绘制）

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Others/images/cm.png" width = "500" />

- 3.10 kalmanfilter.py（卡尔曼滤波）

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Others/images/kf.png" width = "500" />

- 3.11 calc_technical_indicators_formula.py（基于公式计算技术指标）
- 3.12 calc_technical_indicators_TA_LIB.py（基于TA_LIB库计算技术指标）

****

#### 4. Financial-Candle-Picture（金融蜡烛图）

基于`mpl_finance`和`matplotlib`库实现将股价转为蜡烛图，效果预览：

<img src="https://github.com/jm199504/Financial-Time-Series/blob/master/Financial-Candle-Picture/train_pic/002253_0_01.png" width = "200" />

---

#### 5.Financial-Data-Download（金融数据下载）

提供了三种金融数据源：JQdata、akshare、tushare
