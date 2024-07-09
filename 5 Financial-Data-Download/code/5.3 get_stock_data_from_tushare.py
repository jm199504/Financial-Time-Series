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