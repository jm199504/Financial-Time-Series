import tushare as ts
import matplotlib.pyplot as plt
import mpl_finance as mpf
import csv

# 拉取股票历史价格数据
stock_code = '002253'
start_date = '2021-05-01'
end_date = '2021-05-26'
stock_price_data = ts.get_hist_data(stock_code, start=start_date, end=end_date)
stock_price_data.to_csv(f'{stock_code}.csv')
stock_price_data.head()

# 获取趋势标签（上升10/下降01）
pred_days = 1
pic_labels = [''] * len(stock_price_data['close'])
for i in range(pred_days, len(stock_price_data['close'])):
    if (stock_price_data['close'][i] - stock_price_data['close'][i - pred_days]) > 0:
        pic_labels[i] = '10'
    else:
        pic_labels[i] = '01'
stock_price_data['trend_label'] = pic_labels
# stock_price_data.to_csv(f'{stock_code}.csv')

# 生成蜡烛图
file_info = csv.DictReader(open(f'{stock_code}.csv', 'r', encoding='utf-8', errors='ignore'))
dict_data = []
for lines in file_info:
    if file_info.line_num == 1:
        continue
    dict_data.append(lines)

m = 0
data_list = []
while (m < len(dict_data)):
    tempdict = dict_data[m]
    data = (float(m), float(tempdict['open']), float(tempdict['high']), float(tempdict['low']), float(tempdict['close']))
    data_list.append(data)
    m += 1

sliding_day = 10 # sliding windows size
sliding_sum_day = len(data_list) - sliding_day + 1
for i in range(sliding_sum_day):
    d = []
    d.extend(data_list[i:i + sliding_day])
    print(d)
    fig = plt.figure(figsize=(2.24, 2.24))   # pic size is 224 * 224
    ax = fig.add_subplot(111)
    plt.xticks()
    plt.yticks()
    plt.axis("off")
    plt.xlabel("Date")
    plt.ylabel("Price")
    mpf.candlestick_ohlc(ax, d, width=0.3, colorup='r', colordown='green')
    # if i < sliding_sum_day * 0.9:
    #     pic_path = 'train_pic\\' + stock_code + '_' + str(i) + '_' + str(pic_labels[i]) + '.png'
    # else:
    #     pic_path = 'test_pic\\' + stock_code + '_' + str(i) + '_' + str(pic_labels[i]) + '.png'
    # plt.savefig(pic_path, format='png')
    plt.show()
    # plt.close()


