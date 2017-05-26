#!/usr/bin/env python
# -- coding: utf-8 --
import numpy as np
import csv

def fetchdata(trainfile,batch_size,batch_num):
    with open(trainfile) as csvfile:
        read_tr = csv.reader(csvfile,delimiter=',')
        split_loc = batch_size*batch_num
        next(read_tr)
        tra_ans = []
        tra_set = []
        val_ans = []
        val_set = []
        count = 0
        for filein in read_tr:
            tmp = np.array(filein[1].split(' '),float)
            tmp = np.reshape(tmp,(48,48,1))
            if filein[0] == '0':
                tma = [1,0,0,0,0,0,0]
            elif filein[0] == '1':
                tma = [0,1,0,0,0,0,0]
            elif filein[0] == '2':
                tma = [0,0,1,0,0,0,0]
            elif filein[0] == '3':
                tma = [0,0,0,1,0,0,0]
            elif filein[0] == '4':
                tma = [0,0,0,0,1,0,0]
            elif filein[0] == '5':
                tma = [0,0,0,0,0,1,0]
            elif filein[0] == '6':
                tma = [0,0,0,0,0,0,1] 
            if count <split_loc:
                tra_set.append(tmp)
                tra_ans.append(tma)
            else:
                val_set.append(tmp)
                val_ans.append(tma)
            count = count +1
        tra_set=np.array(tra_set)       
        tra_ans=np.array(tra_ans)
        val_set=np.array(val_set)       
        val_ans=np.array(val_ans)
    return [tra_set,tra_ans,val_set,val_ans]

def fetchtest(testfile):
    with open(testfile) as csvfile:
        read_tr = csv.reader(csvfile,delimiter=',')
        next(read_tr)
        val_set = []
        for filein in read_tr:
            tmp = np.array(filein[1].split(' '),int)
            tmp = np.reshape(tmp,(48,48,1))
            val_set.append(tmp)
        val_set=np.array(val_set)       
    return [val_set]
