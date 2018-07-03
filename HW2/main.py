import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt 
(x_train, y_train),(x_test, y_test) = mnist.load_data()  #存取mnist資料

#print(x_train.shape)
#print(y_train.shape)
#print(x_test.shape)
#print(y_test.shape)
x_train = x_train.reshape(60000, 28*28).astype('float32')   #translation of data
x_test = x_test.reshape(10000, 28*28).astype('float32')

x_train /= 255 # Normalization
x_test /= 255
#print(x_train.shape)
#print(x_test.shape)

y_train = keras.utils.to_categorical(y_train, 10) # converting class vectors to binary class matrices
y_test = keras.utils.to_categorical(y_test, 10)

model = Sequential([
    Dense(256, input_shape=(784,)),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])
model.summary()
# model setting
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])  
# training
train_history = model.fit(x=x_train, y=y_train, validation_data=(x_test,y_test), epochs=10, batch_size=200, verbose=2)  

def show_train_history(train_history, train, validation):  #graph of results
    plt.plot(train_history.history[train])  
    plt.plot(train_history.history[validation])  
    plt.title('Train History')  
    plt.ylabel(train)  
    plt.xlabel('Epoch')  
    plt.legend(['train', 'validation'], loc='upper left')  
    plt.show()  
show_train_history(train_history, 'acc', 'val_acc')
show_train_history(train_history, 'loss', 'val_loss')
#evluation
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])