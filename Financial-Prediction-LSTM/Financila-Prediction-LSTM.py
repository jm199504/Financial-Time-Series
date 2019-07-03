import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

import math
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt


# 生成标签值：下一天收盘价（涉及删除最后一条数据，不要重复执行该函数）
def generate_label(data_path):
    df = pd.read_csv(data_path)
    next_close = list()
    for i in range(len(df['close']) - 1):
        next_close.append(df['close'][i + 1])
    next_close.append(0)
    df['next_close'] = next_close
    df.drop(df.index[-1], inplace=True)
    df.to_csv('temp.csv', index=None)

# 生成训练和测试数据
def generate_model_data(data_path,alpha,days):
    df = pd.read_csv(data_path)
    train_day = int((len(df['close']) - days + 1))
    for property in ['open', 'close', 'high', 'low', 'volume','next_close']:
        df[property] = scaler.fit_transform(np.reshape(np.array(df[property]), (-1, 1)))
    X_data, Y_data = list(), list()
    # 生成时序数据
    for i in range(train_day):
        Y_data.append(df['next_close'][i+days-1])
        for j in range(days):
            for m in ['open', 'close', 'high', 'low', 'volume']:
                X_data.append(df[m][i + j])
    X_data = np.reshape(np.array(X_data),(-1,5*15))# 5表示特征数量*天数
    train_length = int(len(Y_data)* alpha)
    X_train = np.reshape(np.array(X_data[:train_length]),(len(X_data[:train_length]),days,5))
    X_test = np.reshape(np.array(X_data[train_length:]),(len(X_data[train_length:]),days,5))
    Y_train,Y_test = np.array(Y_data[:train_length]),np.array(Y_data[train_length:])
    return X_train,Y_train,X_test,Y_test

def calc_MAPE(real,predict):
    Score_MAPE = 0
    for i in range(len(predict[:, 0])):
        Score_MAPE += abs((predict[:, 0][i] - real[:, 0][i]) / real[:, 0][i])
    Score_MAPE = Score_MAPE * 100 / len(predict[:, 0])
    return Score_MAPE

def calc_AMAPE(real,predict):
    Score_AMAPE = 0
    Score_MAPE_DIV = sum(real[:, 0]) / len(real[:, 0])
    for i in range(len(predict[:, 0])):
        Score_AMAPE += abs((predict[:, 0][i] - real[:, 0][i]) / Score_MAPE_DIV)
    Score_AMAPE = Score_AMAPE * 100 / len(predict[:, 0])
    return Score_AMAPE

def evaluate(real,predict):
    RMSE = math.sqrt(mean_squared_error(real[:, 0], predict[:, 0]))
    MAE = mean_absolute_error(real[:, 0], predict[:, 0])
    MAPE = calc_MAPE(real, predict)
    AMAPE = calc_AMAPE(real, predict)
    return RMSE,MAE,MAPE,AMAPE

def lstm_model(X_train, Y_train, X_test, Y_test):
    model = Sequential()
    model.add(LSTM(units=20, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dense(1, activation='hard_sigmoid'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X_train, Y_train, epochs=200, batch_size=20, verbose=1)

    trainPredict = model.predict(X_train)
    trainPredict = scaler.inverse_transform(trainPredict)
    Y_train = scaler.inverse_transform(np.reshape(Y_train, (-1, 1)))

    testPredict = model.predict(X_test)
    testPredict = scaler.inverse_transform(testPredict)
    Y_test = scaler.inverse_transform(np.reshape(Y_test, (-1, 1)))

    return Y_train, trainPredict, Y_test, testPredict
if __name__=='__main__':
    data_path = 'hs300.csv'
    days = 15
    alpha = 0.8
    generate_label(data_path)
    scaler = MinMaxScaler(feature_range=(0, 1))
    X_train, Y_train, X_test, Y_test = generate_model_data('temp.csv',alpha,days)
    train_Y, trainPredict, test_Y, testPredict  = lstm_model(X_train, Y_train, X_test, Y_test)
    plt.plot(list(trainPredict), color='red', label='prediction')
    plt.plot(list(train_Y), color='blue', label='real')
    plt.legend(loc='upper left')
    plt.title('train data')
    plt.show()
    plt.plot(list(testPredict), color='red', label='prediction')
    plt.plot(list(test_Y), color='blue', label='real')
    plt.legend(loc='upper left')
    plt.title('test data')
    plt.show()
    
    RMSE,MAE,MAPE,AMAPE = evaluate(test_Y,testPredict)
    print(RMSE,MAE,MAPE,AMAPE)