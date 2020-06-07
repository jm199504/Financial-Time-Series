from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits as load_data
from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt
import scikitplot as skplt
X, y = load_data(return_X_y=True)
classifier = RandomForestClassifier()
predictions = cross_val_predict(classifier, X, y)
plot = skplt.metrics.plot_confusion_matrix(y, predictions, normalize=True)
plt.show()