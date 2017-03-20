
import csv
import numpy as np
import sys
rows =[]

with open('test_X.csv','rb') as csvfile:
     reader = csv.reader(csvfile)
     lstpm=[]
     for row in reader :
        if row[1] =='PM2.5' :
            lstpm.append(row[3:27])
     print len(lstpm)
