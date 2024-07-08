import matplotlib.pyplot as plt
import mpl_finance as mpf
import pandas as pd
import csv


# 根据股票价格趋势生成标签
# 0 表示下跌趋势，1 表示上涨趋势
def getLabel2Class(stockCode):
    dir_path = 'datas'
    pred_days = 1
    stockPd = pd.read_csv(dir_path + '/' + stockCode + '.csv')  # 读取数据集
    pic_labels = [''] * len(stockPd['close'])
    for i in range(len(stockPd['close']) - pred_days):
        if (stockPd['close'][i + pred_days] - stockPd['close'][i]) > 0:
            pic_labels[i] = '10'  # 上涨标签
        else:
            pic_labels[i] = '01'  # 下跌标签
    stockPd['Lable2Class'] = pic_labels  # 将标签加入数据集
    stockPd.to_csv(dir_path + '/' + stockCode + '.csv')  # 保存更新后的数据集
    return pic_labels


# 处理数据并生成K线图函数
def process_data(stock_code):
    file_info = csv.DictReader(open('datas/' + stock_code + '.csv', 'r', encoding='utf-8', errors='ignore'))
    dict_data = []
    for lines in file_info:
        if file_info.line_num == 1:
            continue
        else:
            dict_data.append(lines)

    data_list = []
    for m in range(len(dict_data)):
        temp_dict = dict_data[m]
        # 提取开盘价、最高价、最低价、收盘价数据
        data = (float(m), float(temp_dict['open']), float(temp_dict['high']), float(temp_dict['low']),
                float(temp_dict['close']))
        data_list.append(data)

    sliding_day = 10  # 滑动窗口大小
    sliding_sum_day = len(data_list) - sliding_day + 1

    for i in range(sliding_sum_day):
        d = []
        d.extend(data_list[i:i + sliding_day])  # 提取滑动窗口内的数据
        fig = plt.figure(figsize=(2.24, 2.24))  # 创建K线图的图像（尺寸为224x224像素）
        ax = fig.add_subplot(111)
        plt.xticks()
        plt.yticks()
        plt.axis("off")  # 关闭坐标轴显示
        plt.xlabel("日期")
        plt.ylabel("价格")
        mpf.candlestick_ohlc(ax, d, width=0.3, colorup='r', colordown='green')  # 绘制K线图
        # 将图像保存为文件，使用适当的命名约定
        pic_path = 'train_pic/' + stock_code + '_' + str(i) + '_' + str(pic_labels[i]) + '.png'
        plt.savefig(pic_path, format='png')  # 保存图像为PNG文件
        plt.close()  # 关闭图像，释放内存


if __name__ == '__main__':
    stockCode = '002253'
    start_data = '2017-01-01'
    end_data = '2017-12-31'
    pic_labels = getLabel2Class(stockCode)  # 生成股票数据的标签
    process_data(stockCode)  # 处理股票数据并生成K线图
