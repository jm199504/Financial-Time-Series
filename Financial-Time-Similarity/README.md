#### 1.pearson_correlation_coefficient

1.1 由于不同股票价格范围差距过大，在进行股票时间序列相似度匹配过程中通常考虑对数差处理，其公式如下所示：

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/pcc1.png" width = "300" />

1.2经过对数差处理后的金融时间序列可表示：

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/pcc2.png" width = "300" />

1.3皮尔逊相关系数计算公式：

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/pcc3.png" width = "300" />

#### 2.dynamic_time_wrapping

2.1 计算两个金融时间序列的时间点对应数据的欧氏距离

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw1.png" width = "300" />

2.2 更新时间点对应数据的距离

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw2.png" width = "300" />

2.3 动态时间规整距离

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw3.png" width = "300" />

2.4 伪代码

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw-alg.png" width = "300" />

2.5 动态时间规整距离输出图举例

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw-draw.png" width = "300" />

2.6 动态时间规整最优匹配对齐

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw-draw2.png" width = "300" />

#### 3.cosine similarity