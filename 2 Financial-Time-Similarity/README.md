#### 1.皮尔逊相关系数（ pearson_correlation_coefficient）

1.1 由于不同股票价格范围差距过大，在进行股票时间序列相似度匹配过程中通常考虑对数差处理，其公式如下所示：

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/pcc1.png" width = "300" />

1.2经过对数差处理后的金融时间序列可表示：

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/pcc2.png" width = "400" />

1.3皮尔逊相关系数计算公式：

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/pcc3.png" width = "600" />

1.4结果

1.4.1相关性较强

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/pcc-result1.png" width = "300" />

1.4.2相关性较弱

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/pcc-result2.png" width = "300" />

#### 2.动态时间规整（dynamic_time_wrapping）

2.1 计算两个金融时间序列的时间点对应数据的欧氏距离

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw1.png" width = "200" />

2.2 更新时间点对应数据的距离

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw2.png" width = "500" />

2.3 动态时间规整距离

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw3.png" width = "200" />

2.4 伪代码

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw-alg.png" width = "600" />

2.5 动态时间规整距离输出图举例

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw-draw.png" width = "400" />

2.6 动态时间规整最优匹配对齐

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw-draw2.png" width = "350" />

2.7结果

2.7.1动态时间规整距离较短

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw-result1.png" width = "300" />

2.7.1动态时间规整距离较长

<img src="https://github.com/jm199504/Financial-Prediction/blob/master/Financial-Time-Similarity/images/dtw-result2.png" width = "300" />

#### 3.余弦相似度（cosine similarity）