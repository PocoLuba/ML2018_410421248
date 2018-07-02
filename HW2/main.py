import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop

(x_train, y_train),(x_test, y_test) = mnist.load_data()  #存取mnist資料

#print(x_train.shape)
#print(y_train.shape)
#print(x_test.shape)
#print(y_test.shape)
x_train = x_train.reshape(60000, 784) #preprocessing image
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255 #reducing dimension
x_test /= 255
print(x_train.shape)
print(x_test.shape)

y_train = keras.utils.to_categorical(y_train, 10) # converting class vectors to binary class matrices
y_test = keras.utils.to_categorical(y_test, 10)

model = Sequential([
    Dense(32, input_shape=(784,)),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])
