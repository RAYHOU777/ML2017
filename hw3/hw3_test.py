#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import argparse
from keras.models import load_model
from termcolor import colored,cprint
from utils import *
from readfile import fetchtest

testfile      = sys.argv[1]
resfile       = sys.argv[2]
#store_path =str(sys.argv[3])
tbatch_size =74

def main():
    model_path = os.path.join('./result1' ,'model.h5')
    emotion_classifier = load_model(model_path)
    emotion_classifier.summary()
    te_feats = fetchtest(testfile)

    ans = emotion_classifier.predict_classes(te_feats)
    with open(resfile,'w') as f:
        f.write('id,label\n')
        for idx,a in enumerate(ans):
            f.write('{},{}\n'.format(idx,a))
    print('\n')

if __name__ == "__main__":
    main()

