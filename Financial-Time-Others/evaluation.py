import math

# 评价指标函数
def Myevalution(prediction,real):
    TP,TN,FP,FN = 0,0,0,0
    for i, j in zip(prediction, real):
        if i == j and i == 1:
            TP+=1
        if i == j and i == 0:
            TN+=1
        if i !=j and i == 1:
            FP+=1
        if i !=j and i == 0:
            FN+=1
    # 准确率Accuracy
    accuracy = (TP+TN) / (TP+TN+FP+FN+0.001)
    # 精确率Precision
    precision = TP / (TP+FP+0.001)
    # 召回率Recall
    recall = TP / (TP+FN+0.001)
    # 特异度Specificity
    specificity = TN / (TN+FP+0.001)
    # 综合评价指标F-measure
    beta = 1
    f_measure = (beta*beta+1)*precision*recall / ((beta*beta)*(precision+recall)+1e-10)
    # MCC
    mcc = ((TP*TN)-(FP*FN))/(math.pow((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN),1/2)+1e-1)
    print('TP:{},TN:{},FP:{},FN:{}'.format(TP,TN,FP,FN))
    print('准确度:{},精确率:{},召回率:{},综合指标:{},MCC:{}'.format(accuracy,precision,recall,f_measure,mcc))
    return TP, TN, FP, FN, accuracy, precision, recall, specificity, f_measure, mcc