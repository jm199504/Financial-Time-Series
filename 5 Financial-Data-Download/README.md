### 5 Financial-Data-Download

金融数据的下载代码（提供了3种金融数据源）

#### 1.从JQdata获取股票数据

```python
from jqdatasdk import *

# 使用JQdata下载CSI300数据
# https://www.joinquant.com/
# 账号及密码请自行前往注册
def downloadCSI300byjqdata():
    auth('18280180192', '**********')
    # security 股票代码 ； frequency 时间粒度（1d=日） ； skip_paused 是否跳过缺失交易数据时间点
    ss = get_price(security='000300.XSHG', start_date='2014-06-03', end_date='2019-11-29', frequency='1d',skip_paused=False)
    ss.to_csv('000300.XSHG.csv')
```



#### 2.从akshare获取股票数据

```python
import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(
    symbol="002253",
    period="daily",
    start_date="20230731",
    end_date='20230731',
    adjust=""
)
print(stock_zh_a_hist_df)
# 开盘价、收盘价、最高价、最低价、成交量、成交额、涨跌幅和换手率

print(f"开盘价：{list(stock_zh_a_hist_df['开盘'].values)}")
print(f"收盘价：{list(stock_zh_a_hist_df['收盘'].values)}")
print(f"最高价：{list(stock_zh_a_hist_df['最高'].values)}")
print(f"最低价：{list(stock_zh_a_hist_df['最低'].values)}")
print(f"成交量：{list(stock_zh_a_hist_df['成交量'].values)}")
print(f"成交额：{list(stock_zh_a_hist_df['成交额'].values)}")
print(f"涨跌幅：{list(stock_zh_a_hist_df['涨跌幅'].values)}")
print(f"换手率：{list(stock_zh_a_hist_df['换手率'].values)}")
```



#### 3.从tushare获取股票数据

```python
import tushare as ts


# 使用Tushare下载CSI300指数所包含的成分股
# http://www.tushare.org/
# token请自行前往注册

def downloadCSI300stocksbytushare():
    token = '35d8848b876df93910413e8936c40745d7b7da42553ae73920862cd9'
    pro = ts.pro_api(token)

    df = pro.daily(ts_code='600519.SH', start_date='20231120', end_date='20231201')  # 川大智能股票


    df = pro.index_weight(index_code='399300.SZ', start_date='20190901', end_date='20190930')  # 沪深300代码
    for i in list(set(df['con_code'])):
        ts.set_token(token)
        # ad 复权类型(qfq-前复权 hfq-后复权 None-不复权，默认为qfq)
        df1 = ts.pro_bar(ts_code=i, adj='qfq', start_date='20160101', end_date='20191201')
        df2 = ts.pro_bar(ts_code=i, adj='qfq', start_date='20000101', end_date='20151231')
        df = pd.concat([df1,df2])
        df = df[::-1]
        df.to_csv('399300.SZ.csv',index=False)
```

