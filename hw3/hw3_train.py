#!/usr/bin/env python
# -- coding: utf-8 --
import numpy as np
import csv
import sys
import os
from readfile import fetchdata
import argparse
from model import build_model
from model import dump_history
from model import History
from utils import *
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping, ModelCheckpoint, CSVLogger
#mport dataprocessing
#=============================================================
# global setting
trainfile      = sys.argv[1]
batch_size=128
batch_num=190
vbatch_size=55
vbatch_num=131
epoch     = 500
store_path =str(sys.argv[2]) 
#=============================================================   
def preprocess_input(images):
    """ preprocess input by substracting the train mean
    # Arguments: images or image of any shape
    # Returns: images or image with substracted train mean (129)
    """
    images = images/255.0
    return images

def main():
    [tra_set,tra_ans,val_set,val_ans] = fetchdata(trainfile,batch_size,batch_num)
    #ra_set =preprocess_input(tra_set)
    #val_set =preprocess_input(val_set)
    print('train set tensor: '+str(tra_set.shape))
    print('train ans tensor: '+str(tra_ans.shape))
    print('valid set tensor: '+str(val_set.shape))
    print('valid ans tensor: '+str(val_ans.shape))
    emotion_classifier = build_model('dnn')
    history = History()
    #csv_logger = CSVLogger('training.log')

    datagen = ImageDataGenerator(
    featurewise_center=False,  # set input mean to 0 over the dataset
    samplewise_center=False,  # set each sample mean to 0
    featurewise_std_normalization=False,  # divide inputs by std of the dataset
    samplewise_std_normalization=False,  # divide each input by its std
    zca_whitening=False,  # apply ZCA whitening
    rotation_range=40,  # randomly rotate images in the range (degrees, 0 to 180)
    width_shift_range=0.2,  # randomly shift images horizontally (fraction of total width)
    height_shift_range=0.2,  # randomly shift images vertically (fraction of total height)
    horizontal_flip=True,  # randomly flip images
    vertical_flip=False)  # randomly flip images
    datagen.fit(tra_set)

    emotion_classifier.fit_generator(datagen.flow(tra_set, tra_ans,
                    batch_size=batch_size),
                    samples_per_epoch=tra_set.shape[0],
                    nb_epoch=epoch,
                    validation_data=(val_set,val_ans),
                    callbacks=[history])
    dump_history(store_path,history)
    emotion_classifier.save(os.path.join(store_path,'model.h5'))
#=============================================================    
if __name__ == "__main__":
    main()

