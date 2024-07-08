import pandas as pd

train_df = pd.read_csv('../data/000001.XSHE.csv')
features = list(train_df.columns)
features.remove('trade_date')  # 移除该字段（影响计算特征方差）
train_df = train_df[features]
for i in train_df.columns:
    print(i,train_df[i].var())
