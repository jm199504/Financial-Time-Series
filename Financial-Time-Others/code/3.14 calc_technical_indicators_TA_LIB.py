import talib
import pandas as pd
import numpy as np
import tushare as ts

code = '000007'
stock = ts.get_k_data(code)
stock.to_csv(code + '.csv')

#计算技术指标
def get_tech(filepath):
    df = pd.read_csv(filepath, index_col='date')
    # Simple Moving Average SMA 简单移动平均
    df['SMA5'] = talib.MA(df['close'],timeperiod=5)
    df['SMA10'] = talib.MA(df['close'], timeperiod=10)
    df['SMA20'] = talib.MA(df['close'], timeperiod=20)
    # Williams Overbought/Oversold Index WR 威廉指标
    df['WR14'] = talib.WILLR(df['high'], df['low'], df['close'], timeperiod=14)
    df['WR18'] = talib.WILLR(df['high'], df['low'], df['close'], timeperiod=18)
    df['WR22'] = talib.WILLR(df['high'], df['low'], df['close'], timeperiod=22)
    # Moving Average Convergence / Divergence MACD 指数平滑移动平均线
    DIFF1, DEA1, df['MACD9'] = talib.MACD(np.array(df['close']),fastperiod=12, slowperiod=26, signalperiod=9)
    DIFF2, DEA2, df['MACD10'] = talib.MACD(np.array(df['close']), fastperiod=14, slowperiod=28, signalperiod=10)
    DIFF3, DEA3, df['MACD11'] = talib.MACD(np.array(df['close']), fastperiod=16, slowperiod=30, signalperiod=11)
    df['MACD9'] = df['MACD9'] * 2
    df['MACD10'] = df['MACD10'] * 2
    df['MACD11'] = df['MACD11'] * 2
    # Relative Strength Index RSI 相对强弱指数
    df['RSI15'] = talib.RSI(np.array(df['close']), timeperiod=15)
    df['RSI20'] = talib.RSI(np.array(df['close']), timeperiod=20)
    df['RSI25'] = talib.RSI(np.array(df['close']), timeperiod=25)
    df['RSI30'] = talib.RSI(np.array(df['close']), timeperiod=30)
    # Stochastic Oscillator Slow STOCH 常用的KDJ指标中的KD指标
    df['STOCH'] = talib.STOCH(df['high'], df['low'], df['close'],fastk_period=9,slowk_period=3,slowk_matype=0,slowd_period=3,slowd_matype=0)[1]
    # On Balance Volume OBV 能量潮
    df['OBV'] = talib.OBV(np.array(df['close']),df['volume'])
    # Simple moving average SMA 简单移动平均
    df['SMA15'] = talib.SMA(df['close'], timeperiod=15)
    df['SMA20'] = talib.SMA(df['close'], timeperiod=20)
    df['SMA25'] = talib.SMA(df['close'], timeperiod=25)
    df['SMA30'] = talib.SMA(df['close'], timeperiod=30)
    # Money Flow Index MFI MFI指标
    df['MFI14'] = talib.MFI(df['high'], df['low'], df['close'],df['volume'], timeperiod=14)
    df['MFI18'] = talib.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod=18)
    df['MFI22'] = talib.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod=22)
    # Ultimate Oscillator UO 终极指标
    df['UO7'] = talib.ULTOSC(df['high'], df['low'], df['close'],  timeperiod1=7, timeperiod2=14, timeperiod3=28)
    df['UO8'] = talib.ULTOSC(df['high'], df['low'], df['close'],  timeperiod1=8, timeperiod2=16, timeperiod3=22)
    df['UO9'] = talib.ULTOSC(df['high'], df['low'], df['close'],  timeperiod1=9, timeperiod2=18, timeperiod3=26)
    # Rate of change Percentage ROCP 价格变化率
    df['ROCP'] = talib.ROCP(df['close'],timeperiod=10)
