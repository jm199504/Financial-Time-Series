from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
import keras
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# for reproducibility
np.random.seed(1337)

# load stock data
df = pd.read_csv('../data/stock.csv')

# normalization
scaler = MinMaxScaler(feature_range=(0, 1))
df['volume'] = scaler.fit_transform(np.reshape(np.array(df['volume']),(-1,1)))
df['close'] = scaler.fit_transform(np.reshape(np.array(df['close']),(-1,1)))
df['low'] = scaler.fit_transform(np.reshape(np.array(df['low']),(-1,1)))
df['high'] = scaler.fit_transform(np.reshape(np.array(df['high']),(-1,1)))
df['open'] = scaler.fit_transform(np.reshape(np.array(df['open']),(-1,1)))

# generate the data format by cnn required
X_data,Y_data = list(),list()
for i in range(len(df['close'])-5):
    for j in range(5):
        X_data.append(df['close'][i+j])
        X_data.append(df['open'][i+j])
        X_data.append(df['high'][i+j])
        X_data.append(df['low'][i+j])
        X_data.append(df['volume'][i+j])

# splite the data to train and test set
X_train = np.array(X_data[:int(len(X_data)*0.5)]).reshape(-1,5,5,1)
X_test = np.array(X_data[int(len(X_data)*0.5):]).reshape(-1,5,5,1)
for i in range(len(df['close'])-5):
    Y_data.append(df['label'][i])
Y_train = np.array(Y_data[:int(len(Y_data)*0.5)]).reshape(-1,1)
Y_test = np.array(Y_data[int(len(Y_data)*0.5):]).reshape(-1,1)
Y_train = keras.utils.to_categorical(Y_train,num_classes=2)
Y_test = keras.utils.to_categorical(Y_test,num_classes=2)

# global variable
batch_size = 10
nb_classes = 2
epochs = 120

# input image dimensions
img_rows, img_cols =  5, 5

# number of convolutional filters to use
nb_filters1 = 32
nb_filters2 = 16

# size of pooling area for max pooling
pool_size = (2, 2)

# convolution kernel size
kernel_size = (3, 3)

# input shape
input_shape = (img_rows, img_cols, 1)

# transfer format
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
Y_train = Y_train.astype('float32')
Y_test = Y_test.astype('float32')

# cnn model with Keras
model = Sequential()
model.add(Convolution2D(nb_filters1, (kernel_size[0], kernel_size[1]),
                        padding='same',
                        input_shape=input_shape,activation='relu'))  # ConV layer 1
model.add(MaxPooling2D(pool_size=pool_size))  # MaxPooling layer
# model.add(Activation('relu'))  # Active layer
model.add(Convolution2D(nb_filters2, (kernel_size[0], kernel_size[1]),padding='same',activation='relu'))  # ConV layer 2
# model.add(Activation('relu'))  # Active layer
model.add(MaxPooling2D(pool_size=pool_size))  # MaxPooling layer
# model.add(Dropout(0.25))  # Dropout
model.add(Flatten())  # Flatten
model.add(Dense(128,activation='relu'))  # Fully connect layer
# model.add(Activation('relu'))  # Active layer
model.add(Dropout(0.5))  # Dropout
model.add(Dense(nb_classes))  # Fully connect layer
model.add(Activation('softmax'))  # Softmax to choose best result

# compile the model
model.compile(loss='categorical_crossentropy',optimizer='adadelta',metrics=['accuracy'])

# fit / train the model
model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs,
          verbose=1)
#validation_data=(X_test, Y_test)

# evaluate the model
score = model.evaluate(X_test, Y_test, verbose=0)
print(model.summary())
prd = model.predict(X_test)
# show the model performance
print('Test score:', score[0])
print('Test accuracy:', score[1])