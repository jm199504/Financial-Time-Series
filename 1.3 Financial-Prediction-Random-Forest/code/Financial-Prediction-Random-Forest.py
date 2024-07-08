from numpy import *
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import warnings
import tushare as ts
import talib
from sklearn import preprocessing


# Get the stock data from tushare
def get_stock_data(code,pred_days):
    df_raw = ts.get_k_data(code)
    # Classification
    label = ['']*len(df_raw['close'])
    for i in range(len(df_raw['close'])-pred_days):
        if (df_raw['close'][i + pred_days] - df_raw['close'][i]) > 0:
            label[i] = 1
        else:
            label[i] = -1
    # Save to typefile file
    df_raw['LABEL'] = label
    # del df_raw['date']
    del df_raw['code']
    df_raw.to_csv('raw_stock.csv', index=None)
    return 'raw_stock.csv'


def exponential_smoothing(alpha, s):
    s2 = np.zeros(s.shape)
    s2[0] = s[0]
    for i in range(1, len(s2)):
        s2[i] = alpha*float(s[i])+(1-alpha)*float(s2[i-1])
    return s2


# preprocess the stock data with exponential_smoothing
def em_stock_data(pathfile, alpha):
    df = pd.read_csv(pathfile)
    es_open = pd.DataFrame(exponential_smoothing(alpha,np.array(df['open'])))
    es_close = pd.DataFrame(exponential_smoothing(alpha, np.array(df['close'])))
    es_high = pd.DataFrame(exponential_smoothing(alpha, np.array(df['high'])))
    es_low = pd.DataFrame(exponential_smoothing(alpha, np.array(df['low'])))
    df['open'],df['close'],df['high'],df['low'] = es_open,es_close,es_high,es_low
    df.to_csv('em_stock.csv',index=None)
    return str('em_stock.csv')


# preprocess the stock data with calc_technical_indicators
def calc_technical_indicators(filepath):
    df = pd.read_csv(filepath, index_col='date')
    # Simple Moving Average SMA 简单移动平均
    df['SMA5'] = talib.MA(df['close'], timeperiod=5)
    df['SMA10'] = talib.MA(df['close'], timeperiod=10)
    df['SMA20'] = talib.MA(df['close'], timeperiod=20)
    # Williams Overbought/Oversold Index WR 威廉指标
    df['WR14'] = talib.WILLR(df['high'], df['low'], df['close'], timeperiod=14)
    df['WR18'] = talib.WILLR(df['high'], df['low'], df['close'], timeperiod=18)
    df['WR22'] = talib.WILLR(df['high'], df['low'], df['close'], timeperiod=22)
    # Moving Average Convergence / Divergence MACD 指数平滑移动平均线
    DIFF1, DEA1, df['MACD9'] = talib.MACD(np.array(df['close']), fastperiod=12, slowperiod=26, signalperiod=9)
    DIFF2, DEA2, df['MACD10'] = talib.MACD(np.array(df['close']), fastperiod=14, slowperiod=28, signalperiod=10)
    df['MACD9'] = df['MACD9'] * 2
    df['MACD10'] = df['MACD10'] * 2
    # Relative Strength Index RSI 相对强弱指数
    df['RSI15'] = talib.RSI(np.array(df['close']), timeperiod=15)
    df['RSI20'] = talib.RSI(np.array(df['close']), timeperiod=20)
    df['RSI25'] = talib.RSI(np.array(df['close']), timeperiod=25)
    df['RSI30'] = talib.RSI(np.array(df['close']), timeperiod=30)
    # Stochastic Oscillator Slow STOCH 常用的KDJ指标中的KD指标
    df['STOCH'] = \
    talib.STOCH(df['high'], df['low'], df['close'], fastk_period=9, slowk_period=3, slowk_matype=0, slowd_period=3,
                slowd_matype=0)[1]
    # On Balance Volume OBV 能量潮
    df['OBV'] = talib.OBV(np.array(df['close']), df['volume'])
    # Simple moving average SMA 简单移动平均
    df['SMA15'] = talib.SMA(df['close'], timeperiod=15)
    df['SMA20'] = talib.SMA(df['close'], timeperiod=20)
    df['SMA25'] = talib.SMA(df['close'], timeperiod=25)
    df['SMA30'] = talib.SMA(df['close'], timeperiod=30)
    # Money Flow Index MFI MFI指标
    df['MFI14'] = talib.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod=14)
    df['MFI18'] = talib.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod=18)
    df['MFI22'] = talib.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod=22)
    # Ultimate Oscillator UO 终极指标
    df['UO7'] = talib.ULTOSC(df['high'], df['low'], df['close'], timeperiod1=7, timeperiod2=14, timeperiod3=28)
    df['UO8'] = talib.ULTOSC(df['high'], df['low'], df['close'], timeperiod1=8, timeperiod2=16, timeperiod3=22)
    df['UO9'] = talib.ULTOSC(df['high'], df['low'], df['close'], timeperiod1=9, timeperiod2=18, timeperiod3=26)
    # Rate of change Percentage ROCP 价格变化率
    df['ROCP'] = talib.ROCP(df['close'], timeperiod=10)
    df.to_csv('final_stock.csv',index=None)
    return 'final_stock.csv'


# preprocess the stock data with normalization and split data
def normalization(filepath, pred_days):
    df= pd.read_csv(filepath)
    df = df[36:(len(df['volume']) - pred_days)]
    features = list(df.T.index)
    features.remove('LABEL')
    # del df['code']
    # normalization
    min_max_scaler = preprocessing.MinMaxScaler()
    for i in range(len(features)):
        df[features[i]] = min_max_scaler.fit_transform(np.reshape(np.array(df[features[i]]),(-1,1)))
    # split data set
    df_len = len(df)
    df_train = df[:int(df_len * 0.8)]
    df_valid = df[int(df_len * 0.8):int(df_len * 0.9)]
    df_test = df[int(df_len * 0.9):]
    df_train.to_csv('train.csv', index=None)
    df_valid.to_csv('valid.csv', index=None)
    df_test.to_csv('test.csv', index=None)
    return 'train.csv', 'valid.csv', 'test.csv', features


def random_forest_model(train_filepath, valid_filepath, test_filepath, features):
    df_train = pd.read_csv(train_filepath)
    df_valid = pd.read_csv(valid_filepath)
    df_test = pd.read_csv(test_filepath)
    alg = RandomForestClassifier(bootstrap=True,min_samples_leaf=2, n_estimators=1000)
    alg.fit(df_train[features],df_train['LABEL'])
    predict = alg.predict(df_valid[features])
    features_degree = sorted(zip(map(lambda x: round(x, 4), alg.feature_importances_),df_train[features]), reverse=True)
    pred_accuracy = (df_valid['LABEL'] == predict).mean()
    return pred_accuracy,features_degree


if __name__=='__main__':
    warnings.filterwarnings(action='ignore', category=DeprecationWarning)
    code = '600585'
    pred_days = 5
    raw_filepath = get_stock_data(code=code, pred_days=pred_days)
    em_filepath = em_stock_data(pathfile=raw_filepath, alpha=0.1)
    final_filepath = calc_technical_indicators(filepath=em_filepath)
    train_filepath, valid_filepath, test_filepath, features = normalization(final_filepath,pred_days=pred_days)
    pred_accuracy, features = random_forest_model(train_filepath, valid_filepath, test_filepath, features)
    print(pred_accuracy)
