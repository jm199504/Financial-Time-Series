# 威廉指标(WR)Williams Overbought/Oversold Index WR 威廉指标
def Williams(df, timeperiod=14):
    wr_indicator = [''] * (timeperiod - 1)
    for i in range(0, len(list(df['volume'])) - timeperiod + 1):
        stock = df[i:timeperiod + i]
        wr_row = (-100) * (max(stock['high']) - stock['close'][-1]) / (max(stock['high']) - min(stock['low']))
        wr_indicator.append(wr_row)
    df['WR'] = wr_indicator


# Stochastic Oscillator SO 随机振荡器
def Stochastic_Oscillator(df, timeperiod=14):
    so_indicator = [''] * (timeperiod - 1)
    for i in range(0, len(list(df['volume'])) - timeperiod + 1):
        stock = df[i:timeperiod + i]
        so_row = 100 * (stock['close'][-1] - min(stock['low'])) / (max(stock['high']) - min(stock['low']))
        so_indicator.append(so_row)
    df['SO'] = so_indicator


# SMA均线
def SMA(df, timeperiod=15):
    sma_indicator = [''] * (timeperiod - 1)
    for i in range(len(df['volume']) - timeperiod + 1):
        stock = df[i:timeperiod + i]
        sma_row = sum(stock['close']) / timeperiod
        sma_indicator.append(sma_row)
    df['SMA'] = sma_indicator


# Price Rate of Change PRC 价格波动率
def Price_Rate_of_Change(df, timeperiod=14):
    prc_indicator = [''] * (timeperiod - 1)
    for i in range(0, len(list(df['volume'])) - timeperiod + 1):
        stock = df[i:timeperiod + i]
        prc_row = (stock['close'][-1] - stock['close'][0]) / (stock['close'][0])
        prc_indicator.append(prc_row)
    df['PRC'] = prc_indicator
