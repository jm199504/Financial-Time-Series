from jqdatasdk import *

# 使用JQdata下载CSI300数据
# https://www.joinquant.com/
# 账号及密码请自行前往注册
def downloadCSI300byjqdata():
    auth('18280180192', '**********')
    # security 股票代码 ； frequency 时间粒度（1d=日） ； skip_paused 是否跳过缺失交易数据时间点
    ss = get_price(security='000300.XSHG', start_date='2014-06-03', end_date='2019-11-29', frequency='1d',skip_paused=False)
    ss.to_csv('000300.XSHG.csv')

