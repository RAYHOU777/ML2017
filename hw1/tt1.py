
         xd_0 = lstpm[i][0] 
         xd_1 = lstpm[i][1]  
         xd_2 = lstpm[i][2]  
         xd_3 = lstpm[i][3]  
         xd_4 = lstpm[i][4]  
         xd_5 = lstpm[i][5]  
         xd_6 = lstpm[i][6]  
         xd_7 = lstpm[i][7]  
         xd_8 = lstpm[i][8] 
         yd   = lstpm[i][9]
         b = -120
         w0 = 0.5
         w1 = 0.5
         w2 = 0.5
         w3 = 0.5
         w4 = 0.5
         w5 = 0.5
         w6 = 0.5
         w7 = 0.5
         w8 = 0.5
         lr = 1

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
         iteration = 10000
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
         for r in range(iteration):
             b_grad = 0
             w0_grad = 0
             w1_grad = 0
             w2_grad = 0
             w3_grad = 0
             w4_grad = 0
             w5_grad = 0
             w6_grad = 0
             w7_grad = 0
             w8_grad = 0


             for n in range(len(x_data)):
                 b_grad = b_grad  - 2.0*(yd[n] - b - w0*xd_0 - w1*xd_1 - w2*xd_2 - w3*xd_3 - w4*xd_4 - w5*xd_5 - w6*xd_6 - w7*xd_7 - w8*xd_8)*1.0
                 w0_grad = w_grad  - 2.0*(yd[n] - b - w0*xd_0 - w1*xd_1 - w2*xd_2 - w3*xd_3 - w4*xd_4 - w5*xd_5 - w6*xd_6 - w7*xd_7 - w8*xd_8)*xd_0
                 w1_grad = w_grad  - 2.0*(yd[n] - b - w0*xd_0 - w1*xd_1 - w2*xd_2 - w3*xd_3 - w4*xd_4 - w5*xd_5 - w6*xd_6 - w7*xd_7 - w8*xd_8)*xd_1
                 w2_grad = w_grad  - 2.0*(yd[n] - b - w0*xd_0 - w1*xd_1 - w2*xd_2 - w3*xd_3 - w4*xd_4 - w5*xd_5 - w6*xd_6 - w7*xd_7 - w8*xd_8)*xd_2
                 w3_grad = w_grad  - 2.0*(yd[n] - b - w0*xd_0 - w1*xd_1 - w2*xd_2 - w3*xd_3 - w4*xd_4 - w5*xd_5 - w6*xd_6 - w7*xd_7 - w8*xd_8)*xd_3
                 w4_grad = w_grad  - 2.0*(yd[n] - b - w0*xd_0 - w1*xd_1 - w2*xd_2 - w3*xd_3 - w4*xd_4 - w5*xd_5 - w6*xd_6 - w7*xd_7 - w8*xd_8)*xd_4
                 w5_grad = w_grad  - 2.0*(yd[n] - b - w0*xd_0 - w1*xd_1 - w2*xd_2 - w3*xd_3 - w4*xd_4 - w5*xd_5 - w6*xd_6 - w7*xd_7 - w8*xd_8)*xd_5
                 w6_grad = w_grad  - 2.0*(yd[n] - b - w0*xd_0 - w1*xd_1 - w2*xd_2 - w3*xd_3 - w4*xd_4 - w5*xd_5 - w6*xd_6 - w7*xd_7 - w8*xd_8)*xd_6
                 w7_grad = w_grad  - 2.0*(yd[n] - b - w0*xd_0 - w1*xd_1 - w2*xd_2 - w3*xd_3 - w4*xd_4 - w5*xd_5 - w6*xd_6 - w7*xd_7 - w8*xd_8)*xd_7
                 w8_grad = w_grad  - 2.0*(yd[n] - b - w0*xd_0 - w1*xd_1 - w2*xd_2 - w3*xd_3 - w4*xd_4 - w5*xd_5 - w6*xd_6 - w7*xd_7 - w8*xd_8)*xd_8
         
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

             b = b -lr/np.squr(b_lr) * b_grad
             w0 = w0 -lr/np.squr(w0_lr) * w0_grad
             w1 = w1 -lr/np.squr(w1_lr) * w1_grad
             w2 = w2 -lr/np.squr(w2_lr) * w2_grad
             w3 = w3 -lr/np.squr(w3_lr) * w3_grad
             w4 = w4 -lr/np.squr(w4_lr) * w4_grad
             w5 = w5 -lr/np.squr(w5_lr) * w5_grad
             w6 = w6 -lr/np.squr(w6_lr) * w6_grad
             w7 = w7 -lr/np.squr(w7_lr) * w7_grad
             w8 = w8 -lr/np.squr(w8_lr) * w8_grad

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











         i+=1


