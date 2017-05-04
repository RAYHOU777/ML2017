import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from keras.models import Sequential
from keras.layers import Input,Dense,Dropout,Flatten,merge,Activation,BatchNormalization
from keras.layers import Convolution2D,MaxPooling2D, AveragePooling2D, ZeroPadding2D,PReLU,ELU
from keras.regularizers import l2
from keras.optimizers import SGD,Adam,Adadelta,Nadam
from keras.models import Model
nb_class = 7
from keras import backend as K
from keras.callbacks import Callback
import keras
from keras.initializers import  RandomNormal
def build_model(mode):


    model = Sequential()
    if mode == 'easy':
        # CNN part (you can repeat this part several times)
        model.add(Convolution2D(8,1,1,border_mode='valid',input_shape=(48,48,1)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.8))

        # Fully connected part
        model.add(Flatten())
        model.add(Dense(16))
        model.add(Activation('relu'))
        model.add(Dense(nb_class))
        model.add(Activation('softmax'))
        opt = SGD(lr=0.01,decay=0.0)
    if mode == 'cnn':

        
        model.add(Convolution2D(64, 5, 5, border_mode='valid',input_shape=(48, 48,1)))
        model.add(PReLU(init='zero', weights=None))
        model.add(ZeroPadding2D(padding=(2, 2)))
        model.add(MaxPooling2D(pool_size=(5, 5),strides=(2, 2)))

        model.add(ZeroPadding2D(padding=(1, 1))) 
        model.add(Convolution2D(64, 3, 3))
        model.add(PReLU(init='zero', weights=None))
        model.add(ZeroPadding2D(padding=(1, 1)))

        model.add(Convolution2D(64, 3, 3))
        model.add(PReLU(init='zero', weights=None))
        model.add(AveragePooling2D(pool_size=(3, 3),strides=(2, 2)))

        model.add(ZeroPadding2D(padding=(1, 1)))
        model.add(Convolution2D(128, 3, 3))
        model.add(PReLU(init='zero', weights=None))
        model.add(ZeroPadding2D(padding=(1, 1)))
        model.add(Convolution2D(128, 3, 3))
        model.add(PReLU(init='zero', weights=None))

        model.add(ZeroPadding2D(padding=(1, 1)))
        model.add(AveragePooling2D(pool_size=(3, 3),strides=(2, 2)))
        #opt = Adadelta(lr=0.1, rho=0.95, epsilon=1e-08)

        model.add(Flatten())
        model.add(Dense(1024))
        model.add(PReLU(init='zero', weights=None))
        model.add(Dropout(0.2))
        model.add(Dense(1024))
        model.add(PReLU(init='zero', weights=None))
        model.add(Dropout(0.2))
        model.add(Dense(7))
        model.add(Activation('softmax'))


        opt = Adadelta(lr=0.1, rho=0.95, epsilon=1e-08)    


    if mode == 'dnn':

        model.add(Dense(input_dim=1*2304,units=512))
        model.add(PReLU(init='zero', weights=None))
        model.add(Dropout(0.2))
        model.add(Dense(512))
        model.add(PReLU(init='zero', weights=None))
        model.add(Dropout(0.1))
        model.add(Dense(512))
        model.add(PReLU(init='zero', weights=None))
        model.add(Dropout(0.1))
        model.add(Dense(7))
        model.add(Activation('softmax'))

        opt = Adadelta(lr=0.1, rho=0.95, epsilon=1e-08)    


    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])

    model.summary() # show the whole model in terminal
    return model

def dump_history(store_path,logs):
    with open(os.path.join(store_path,'train_loss'),'a') as f:
        for loss in logs.tr_losses:
            f.write('{}\n'.format(loss))
    with open(os.path.join(store_path,'train_accuracy'),'a') as f:
        for acc in logs.tr_accs:
            f.write('{}\n'.format(acc))
    with open(os.path.join(store_path,'valid_loss'),'a') as f:
        for loss in logs.val_losses:
            f.write('{}\n'.format(loss))
    with open(os.path.join(store_path,'valid_accuracy'),'a') as f:
        for acc in logs.val_accs:
            f.write('{}\n'.format(acc))

class History(Callback):
    def on_train_begin(self,logs={}):
        self.tr_losses=[]
        self.val_losses=[]
        self.tr_accs=[]
        self.val_accs=[]

    def on_epoch_end(self,epoch,logs={}):
        self.tr_losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.tr_accs.append(logs.get('acc'))
        self.val_accs.append(logs.get('val_acc'))
