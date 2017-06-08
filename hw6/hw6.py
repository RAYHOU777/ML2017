
import csv
import numpy as np
import pandas as pd
import sys

P_p = np.load('P_pred.npy')
Q_p = np.load('Q_pred.npy')
P_b = np.load('P_bias.npy')
Q_b = np.load('Q_bias.npy')

print P_p.shape
#print Q_p
#print P_b
#print Q_b
#--------------------------validition
idall = 100337
ppval = P_p[:1000]
pptra = P_p[1000:]
qpval = Q_p[:1000]
qptra = Q_p[1000:]
pbval = P_b[:1000]
pbtra = P_b[1000:]
qbval = Q_b[:1000]
qbtra = Q_b[1000:]

data_path = sys.argv[1]
pred_path = sys.argv[2]
#output_path = sys.argv[3]

#---------------------------------------

############################### prediction

f_pred = open(pred_path , 'wb')
writer = csv.writer(f_pred, delimiter=',')
writer.writerow(['TestDataID','Rating'])

#pred = np.dot(ppval, qpval)
#print pred

with open(data_path+'test.csv', 'rb') as f:
    fin = csv.reader(f)
    next(fin)
    for i in range(1, idall):
        row = next(fin)
        id_user = int(row[1])
        id_movi = int(row[2])
        rate_pred = np.dot(P_p[id_user-1,], (Q_p[id_movi-1, ].T))+P_b[id_user-1]+Q_b[id_movi-1]
       # rate_pred = np.dot(P_p[id_user-1,], (Q_p[id_movi-1, ].T))]
        if rate_pred[0] > 5.0:
            rate_pred[0] = 5

        writer.writerow([i,  rate_pred[0]])

