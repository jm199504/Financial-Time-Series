import tushare as ts
from jqdatasdk import *

# 使用Tushare下载CSI300指数所包含的成分股
# http://www.tushare.org/
# token请自行前往注册
def downloadCSI300stocksbytushare():
    token = '35d8848b876df939104************2553ae73920862cd9'
    pro = ts.pro_api(token)
    df = pro.index_weight(index_code='399300.SZ', start_date='20190901', end_date='20190930')#沪深300代码
    for i in list(set(df['con_code'])):
        ts.set_token(token)
        # ad 复权类型(qfq-前复权 hfq-后复权 None-不复权，默认为qfq)
        df1 = ts.pro_bar(ts_code=i, adj='qfq', start_date='20160101', end_date='20191201')
        df2 = ts.pro_bar(ts_code=i, adj='qfq', start_date='20000101', end_date='20151231')
        df = pd.concat([df1,df2])
        df = df[::-1]
        df.to_csv('399300.SZ.csv',index=False)

# 使用JQdata下载CSI300数据
# https://www.joinquant.com/
# 账号及密码请自行前往注册
def downloadCSI300byjqdata():
    auth('18280180192', '**********')
    # security 股票代码 ； frequency 时间粒度（1d=日） ； skip_paused 是否跳过缺失交易数据时间点
    ss = get_price(security='000300.XSHG', start_date='2014-06-03', end_date='2019-11-29', frequency='1d',skip_paused=False)
    ss.to_csv('000300.XSHG.csv')

