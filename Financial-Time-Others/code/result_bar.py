import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

ratiolist1 = [56.00, 57.71, 56.28, 56.66]
ratiolist2 = [56.65, 58.10, 55.82, 56.86]
ratiolist3 = [69.53, 63.89, 75.54, 69.65]
ratiolist4 = [62.39, 60.71, 64.09, 62.40]
models = [0] * len(ratiolist1)#标注模型名称
ratiolist = [ratiolist1,ratiolist2,ratiolist3,ratiolist4]

fontsize = 36# 文字大小
smallsize = 32#图例字体大小
width = 3.0# 图柱宽度
gap = width# 图柱间隔
dis = 2.5# 将模型名称标注左移
cgap = 20# 各模型之间的宽度

plt.figure(figsize=(36, 12))
x = []

for i in range(0, len(ratiolist1)):
    x.append(i * cgap)
model_list = ['模型1', '模型2', '模型3','模型4']
class_list = ['准确率', '准确率', '召回率', 'F1度量']
color_list = ['#8ac6d1','#ff9d76','#0f4c81','#eb4d55']
for i in range(0,len(ratiolist1)):
    plt.bar(x, ratiolist[i], label=class_list[i], fc=color_list[i], width=width)
    for j in range(len(x)):
        x[j] = x[j] + gap


for i in range(len(x)):
    x[i] = x[i] - dis * gap

plt.bar(x, models, fc='b', tick_label=model_list)
plt.xlabel('预测模型',fontsize=fontsize)
plt.ylabel('百分比(%)',fontsize=fontsize)
plt.ylim(0, 100)
plt.xticks(fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.legend(fontsize=smallsize)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()
