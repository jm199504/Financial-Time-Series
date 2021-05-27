import numpy as np
import matplotlib.pyplot as plt

classes = ['P', 'N']
confusion_matrix = np.array([(9, 1, ), (2, 13, ),],dtype=np.int)
plt.rcParams['font.sans-serif']=['SimHei']
plt.imshow(confusion_matrix, interpolation='nearest', cmap=plt.cm.Oranges)  # 按照像素显示出矩阵
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes)
plt.yticks(tick_marks, classes)
thresh = confusion_matrix.max() / 2.
fontsize = 15

iters = np.reshape([[[i, j] for j in range(2)] for i in range(2)], (confusion_matrix.size, 2))
for i, j in iters:
    plt.text(j, i, format(confusion_matrix[i, j]),fontsize=fontsize)  # 显示对应的数字

plt.ylabel('真实结果',fontsize=fontsize)
plt.xlabel('预测结果',fontsize=fontsize)
plt.title('混淆矩阵',fontsize=15)
plt.tight_layout()
plt.show()