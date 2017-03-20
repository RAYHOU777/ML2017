

import csv
import numpy as np
import sys
rows =[]

with open('train.csv','rb') as csvfile:
     reader = csv.reader(csvfile)
     lstpm = []
     lstpm10 = []
     for row in reader :
        if row[2] =='PM2.5' :
            lstpm.append(row[3:27])
        if row[2] =='SO2' :
            lstpm10.append(row[3:27])

    # print len(lstpm)
    # print lstpm10[1]
     xd_0 = []     
     xd_1 = []
     xd_2 = []
     xd_3 = []
     xd_4 = []
     xd_5 = []
     xd_6 = []
     xd_7 = []
     xd_8 = []
     xd10_0 = []
     xd10_1 = []
     xd10_2 = []
     xd10_3 = []
     xd10_4 = []
     xd10_5 = []
     xd10_6 = []
     xd10_7 = []
     xd10_8 = []
     yd  = []

     i=0
     while i < len(lstpm) :
         xd_0.insert(i,int(lstpm[i][0]))
         xd_1.insert(i,int(lstpm[i][1]))
         xd_2.insert(i,int(lstpm[i][2]))
         xd_3.insert(i,int(lstpm[i][3]))
         xd_4.insert(i,int(lstpm[i][4]))
         xd_5.insert(i,int(lstpm[i][5]))
         xd_6.insert(i,int(lstpm[i][6]))
         xd_7.insert(i,int(lstpm[i][7]))
         xd_8.insert(i,int(lstpm[i][8]))
         xd10_0.insert(i,float(lstpm10[i][0]))
         xd10_1.insert(i,float(lstpm10[i][1]))
         xd10_2.insert(i,float(lstpm10[i][2]))
         xd10_3.insert(i,float(lstpm10[i][3]))
         xd10_4.insert(i,float(lstpm10[i][4]))
         xd10_5.insert(i,float(lstpm10[i][5]))
         xd10_6.insert(i,float(lstpm10[i][6]))
         xd10_7.insert(i,float(lstpm10[i][7]))
         xd10_8.insert(i,float(lstpm10[i][8]))

         yd.insert(i,int(lstpm[i][9]))
         i+=1
    # print yd

     b =  0.1
     w0 = 0.1
     w1 = 0.1
     w2 = 0.1
     w3 = 0.1
     w4 = 0.1
     w5 = 0.1
     w6 = 0.1
     w7 = 0.1
     w8 = 0.1
     w00 = 0.1
     w01 = 0.1
     w02 = 0.1
     w03 = 0.1
     w04 = 0.1
     w05 = 0.1
     w06 = 0.1
     w07 = 0.1
     w08 = 0.1
     lr = 0.1
     b_history = [b] 
     w0_history = [w0]
     w1_history = [w1]
     w2_history = [w2]
     w3_history = [w3]
     w4_history = [w4]
     w5_history = [w5]
     w6_history = [w6]
     w7_history = [w7]
     w8_history = [w8]
     w00_history = [w00]
     w01_history = [w01]
     w02_history = [w02]
     w03_history = [w03]
     w04_history = [w04]
     w05_history = [w05]
     w06_history = [w06]
     w07_history = [w07]
     w08_history = [w08]
     iteration = 5000
     b_lr = 0
     w0_lr = 0
     w1_lr = 0
     w2_lr = 0
     w3_lr = 0
     w4_lr = 0
     w5_lr = 0
     w6_lr = 0
     w7_lr = 0
     w8_lr = 0
     w00_lr = 0
     w01_lr = 0
     w02_lr = 0
     w03_lr = 0
     w04_lr = 0
     w05_lr = 0
     w06_lr = 0
     w07_lr = 0
     w08_lr = 0
     for r in range(iteration):
         b_grad = 0.0
         w0_grad = 0.0
         w1_grad = 0.0
         w2_grad = 0.0
         w3_grad = 0.0
         w4_grad = 0.0
         w5_grad = 0.0
         w6_grad = 0.0
         w7_grad = 0.0
         w8_grad = 0.0
         w00_grad = 0.0
         w01_grad = 0.0
         w02_grad = 0.0
         w03_grad = 0.0
         w04_grad = 0.0
         w05_grad = 0.0
         w06_grad = 0.0
         w07_grad = 0.0
         w08_grad = 0.0

         for n in range(len(xd_0)):

             b_grad = b_grad  - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*1.0
             w0_grad = w0_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd_0[n]
             w1_grad = w1_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd_1[n]
             w2_grad = w2_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd_2[n]
             w3_grad = w3_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd_3[n]
             w4_grad = w4_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd_4[n]
             w5_grad = w5_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd_5[n]
             w6_grad = w6_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd_6[n]
             w7_grad = w7_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd_7[n]
             w8_grad = w8_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd_8[n]
             w00_grad = w00_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd10_0[n]
             w01_grad = w01_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd10_1[n]
             w02_grad = w02_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd10_2[n]
             w03_grad = w03_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd10_3[n]
             w04_grad = w04_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd10_4[n]
             w05_grad = w05_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd10_5[n]
             w06_grad = w06_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd10_6[n]
             w07_grad = w07_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd10_7[n]
             w08_grad = w08_grad - 2.0*(yd[n] - b - w0*xd_0[n] - w1*xd_1[n] - w2*xd_2[n] - w3*xd_3[n] - w4*xd_4[n] - w5*xd_5[n] - w6*xd_6[n] - w7*xd_7[n] - w8*xd_8[n]- w00*xd10_0[n] - w01*xd10_1[n] - w02*xd10_2[n] - w03*xd10_3[n] - w04*xd10_4[n] - w05*xd10_5[n] - w06*xd10_6[n] - w07*xd10_7[n] - w08*xd10_8[n])*xd10_8[n]
         
         b_lr = b_lr + b_grad**2
         w0_lr = w0_lr + w0_grad**2
         w1_lr = w1_lr + w1_grad**2
         w2_lr = w2_lr + w2_grad**2
         w3_lr = w3_lr + w3_grad**2
         w4_lr = w4_lr + w4_grad**2
         w5_lr = w5_lr + w5_grad**2
         w6_lr = w6_lr + w6_grad**2
         w7_lr = w7_lr + w7_grad**2
         w8_lr = w8_lr + w8_grad**2
         w00_lr = w00_lr + w00_grad**2
         w01_lr = w01_lr + w01_grad**2
         w02_lr = w02_lr + w02_grad**2
         w03_lr = w03_lr + w03_grad**2
         w04_lr = w04_lr + w04_grad**2
         w05_lr = w05_lr + w05_grad**2
         w06_lr = w06_lr + w06_grad**2
         w07_lr = w07_lr + w07_grad**2
         w08_lr = w08_lr + w08_grad**2


         b = b -lr/np.sqrt(b_lr) * b_grad
         w0 = w0 -lr/np.sqrt(w0_lr) * w0_grad
         w1 = w1 -lr/np.sqrt(w1_lr) * w1_grad
         w2 = w2 -lr/np.sqrt(w2_lr) * w2_grad
         w3 = w3 -lr/np.sqrt(w3_lr) * w3_grad
         w4 = w4 -lr/np.sqrt(w4_lr) * w4_grad
         w5 = w5 -lr/np.sqrt(w5_lr) * w5_grad
         w6 = w6 -lr/np.sqrt(w6_lr) * w6_grad
         w7 = w7 -lr/np.sqrt(w7_lr) * w7_grad
         w8 = w8 -lr/np.sqrt(w8_lr) * w8_grad
         w00 = w00 -lr/np.sqrt(w00_lr) * w00_grad
         w01 = w01 -lr/np.sqrt(w01_lr) * w01_grad
         w02 = w02 -lr/np.sqrt(w02_lr) * w02_grad
         w03 = w03 -lr/np.sqrt(w03_lr) * w03_grad
         w04 = w04 -lr/np.sqrt(w04_lr) * w04_grad
         w05 = w05 -lr/np.sqrt(w05_lr) * w05_grad
         w06 = w06 -lr/np.sqrt(w06_lr) * w06_grad
         w07 = w07 -lr/np.sqrt(w07_lr) * w07_grad
         w08 = w08 -lr/np.sqrt(w08_lr) * w08_grad
         

         b_history.append(b)
         w0_history.append(w0)
         w1_history.append(w1)
         w2_history.append(w2)
         w3_history.append(w3)
         w4_history.append(w4)
         w5_history.append(w5)
         w6_history.append(w6)
         w7_history.append(w7)
         w8_history.append(w8)
         w00_history.append(w00)
         w01_history.append(w01)
         w02_history.append(w02)
         w03_history.append(w03)
         w04_history.append(w04)
         w05_history.append(w05)
         w06_history.append(w06)
         w07_history.append(w07)
         w08_history.append(w08)

         #print w01
with open('test_X.csv','rb') as csvfile:
     reader = csv.reader(csvfile)
     lstpm1=[]
     lstpm110=[]
     for row1 in reader :
        if row1[1] =='PM2.5' :
            lstpm1.append(row1[2:27])
        if row1[1] =='SO2' :
            lstpm110.append(row1[2:27])
    # print lstpm110[1]
     xd_0 = []
     xd_1 = []
     xd_2 = []
     xd_3 = []
     xd_4 = []
     xd_5 = []
     xd_6 = []
     xd_7 = []
     xd_8 = []
     xd_00 = []
     xd_01 = []
     xd_02 = []
     xd_03 = []
     xd_04 = []
     xd_05 = []
     xd_06 = []
     xd_07 = []
     xd_08 = []
     y_out = []
     y_num = []
     y=0
     q=0
     yy=[]
     while q < len(lstpm) :
         xd_0.insert(q,int(lstpm1[q][0]))
         xd_1.insert(q,int(lstpm1[q][1]))
         xd_2.insert(q,int(lstpm1[q][2]))
         xd_3.insert(q,int(lstpm1[q][3]))
         xd_4.insert(q,int(lstpm1[q][4]))
         xd_5.insert(q,int(lstpm1[q][5]))
         xd_6.insert(q,int(lstpm1[q][6]))
         xd_7.insert(q,int(lstpm1[q][7]))
         xd_8.insert(q,int(lstpm1[q][8]))
         xd_00.insert(q,float(lstpm110[q][0]))
         xd_01.insert(q,float(lstpm110[q][1]))
         xd_02.insert(q,float(lstpm110[q][2]))
         xd_03.insert(q,float(lstpm110[q][3]))
         xd_04.insert(q,float(lstpm110[q][4]))
         xd_05.insert(q,float(lstpm110[q][5]))
         xd_06.insert(q,float(lstpm110[q][6]))
         xd_07.insert(q,float(lstpm110[q][7]))
         xd_08.insert(q,float(lstpm110[q][8]))
         q+=1

     id = ['id','value']
     f= open('test_x11.csv','w')
     w=csv.writer(f)
     w.writerow(id)
     for n in range(len(xd_0)):

         y =   b + w0*xd_0[n] + w1*xd_1[n] + w2*xd_2[n] + w3*xd_3[n] + w4*xd_4[n] + w5*xd_5[n] + w6*xd_6[n] + w7*xd_7[n] + w8*xd_8[n]+ w00*xd_00[n] + w01*xd_01[n] + w02*xd_02[n] + w03*xd_03[n] + w04*xd_04[n] + w05*xd_05[n] + w06*xd_06[n] + w07*xd_07[n] + w08*xd_08[n]
         y_out.insert(n,y)
         y_num.insert(n,'id_'+str(n))  
   #  print y_out
   #  w.writerows('id_')
     w.writerows(zip(y_num,y_out))

    


     f.close







     



         



 







