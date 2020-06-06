import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

ratiolist1 = [49.46,50.25,50.79,54.79,63.52]
ratiolist2 = [58.82,55.33,52.06,46.79,52.78]
ratiolist3 = [57.53,50.97,54.29,58.53,66.00]
ratiolist4 = [69.97,66.62,55.69,58.43,50.27]
ratiolist5 = [64.54,73.63,60.29,68.14,58.67]
ratiolist = [ratiolist1,ratiolist2,ratiolist3,ratiolist4,ratiolist5]
model_list = ['模型1','模型1','模型1','模型1','模型5']
code_list = ['000001','000408','000538','600482','600583']
sc_list = ['v','8','s','x','o','<']
fontsize = 26
smallsize = 18
mgap = 13
width = 3.0
gap = width
s = 100
ratiolist6 = [0]*len(ratiolist1)
plt.figure(figsize=(16, 9))
x = []
for i in range(len(model_list)):
    x.append(i*mgap)

for i in range(len(model_list)):
    plt.plot(x, ratiolist[i])
    plt.scatter(x, ratiolist[i],marker=sc_list[i],s=s, label=model_list[i])

plt.grid()#网格背景
plt.bar(x, ratiolist6,fc = 'b',tick_label =code_list)


plt.xlabel('股票代码',fontsize=fontsize)
plt.ylabel('F1度量(%)',fontsize=fontsize)
plt.ylim(40,90)

my_y_ticks = np.arange(40,90,10)
plt.xticks(fontsize=fontsize)
plt.yticks(my_y_ticks,fontsize=fontsize)
plt.legend(fontsize=smallsize,loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()
