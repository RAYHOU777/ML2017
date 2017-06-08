import csv
import numpy as np
import pandas as pd

import random


def get_embedding_dict(path):
    embedding_dict = {}
    with open(path,'r') as f:
        for line in f:
            values = line.split(' ')
            word = values[0]
            coefs = np.asarray(values[1:],dtype='float32')
            embedding_dict[word] = coefs
    return embedding_dict

def feature_normalize(X_train, X_test):
	# feature normalization with all X
	X_all = np.concatenate((X_train, X_test))
	mu = np.mean(X_all, axis=0)
	sigma = np.std(X_all, axis=0)
	
	# only apply normalization on continuos attribute
	index = [0, 1, 3, 4, 5]
	mean_vec = np.zeros(X_all.shape[1])
	std_vec = np.ones(X_all.shape[1])
	mean_vec[index] = mu[index]
	std_vec[index] = sigma[index]

	X_all_normed = (X_all - mean_vec) / std_vec

	# split train, test again
	X_train_normed = X_all_normed[0:X_train.shape[0]-1]

	X_test_normed = X_all_normed[X_train.shape[0]:]

	return X_train_normed, X_test_normed

def matrix_factorization(R, P, Q, K, steps=50, alpha=0.0001, beta=0.1):
    Q = Q.T
    vp = [[[0.] for c in range(K)] for r in range(rows)]
    vp = np.array(vp).reshape(rows, K)

    vpp = [[[0.] for c in range(K)] for r in range(rows)]
    vpp = np.array(vpp).reshape(rows, K)
   
    vq = [[[0.] for c in range(K)] for r in range(cols)]
    vq = np.array(vq).reshape(cols, K).T
#    print vq
    vqq = [[[0.] for c in range(K)] for r in range(cols)]
    vqq = np.array(vqq).reshape(cols, K).T

    biasp = [[0.] for c in range(rows)]
    biasq = [[0.] for c in range(cols)]
    biasp = np.array(biasp)
    biasq = np.array(biasq)

#    print biasq 
#    print biasp

    biasp_v = [[0.] for c in range(rows)]
    biasq_v = [[0.] for c in range(rows)]
    biasp_v = np.array(biasp_v)
    biasq_v = np.array(biasq_v)
#    print biasp_v.shape
#    print biasp_v
#    print biasq_v.shape
#    print biasq_v
#    print P.shape
#    print Q.shape

    b = 0.98
    bb = 0.95
    b1 = bb*b


    for step in xrange(steps):
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):

                if R[i][j] > 0:
                    eij = R[i][j] - (np.dot(P[i,:],Q[:,j]) + biasp[i] + biasq[j])
                   
                    for k in xrange(K):
        
                        vp[i][k] = b*vp[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        vq[k][j] = b*vq[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
                        biasp_v[i] = b*biasp_v[i] + alpha *(2 * eij)*0.0001
                        biasq_v[j] = b*biasq_v[j] + alpha *(2 * eij)*0.0001
                        #P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        #Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
                        P[i][k] = P[i][k] + vp[i][k]
                        Q[k][j] = Q[k][j] + vq[k][j]
                        biasp[i] = biasp[i] + biasp_v[i]
                        biasq[j] = biasq[j] + biasq_v[j]
        #eR = np.dot(P,Q)
        e = 0
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - np.dot(P[i,:],Q[:,j]), 2)
                   # for k in xrange(K):
                   #     e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )

        e = e/899873
        print ('step: ' + str(step) + ', err: ' + str(e))
        if e < 0.01:
            break
    return P, Q.T, biasp, biasq




r = 6040
c = 3952
rows = 6040
cols = 3952


R = [[[0] for c in range(cols)] for r in range(rows)]
R = np.array(R)


with open('train.csv', 'rb') as f:
    fin = csv.reader(f)
    print next(fin)
    usr = []
    movi = []
    i = 0
    for row in fin:
    #for i in range(5):
        #row = next(fin)
        id_user = int(row[1])-1
        usr.insert(i,id_user)
        id_movi = int(row[2])-1
        movi.insert(i,id_movi)
        rating  = int(row[3])
        R[id_user, id_movi] = rating
   #     R[id_user, id_movi] =random.randint(1,5)
        i=i+1
       
#print movi
RR = R.reshape(rows, cols)
#print usr
R = R.reshape(rows, cols)
print R.shape

#feature_normalize(usr, movi)
#------------------nor--------------------------------------

mu = np.mean(R, axis=0)
sigma = np.std(R, axis=0)
usr_mu = np.mean(usr, axis=0)
usr_sigma = np.std(usr, axis=0)
#print mu
movi_sigma = np.std(movi, axis=0)
movi_mu = np.mean(movi, axis=0)
#print sigma
#print mu.shape
#print sigma
#print sigma.shape
#normed = (R - mu) / sigma
#print normed
#print normed.shape

#-----------------------------------------------------------



kk = 16
P = np.random.rand(rows,kk)
Q = np.random.rand(cols,kk)

#print p.shape
#print p

P_pred, Q_pred, P_bias, Q_bias = matrix_factorization(R, P, Q, kk)
#P_pred_new, Q_pred_new, P_bias_new, Q_bias_new = matrix_factorization(normed, P, Q, kk)
#np.save('P_pred_new.npy', P_pred_new)
#np.save('Q_pred_new.npy', Q_pred_new)
#np.save('P_bias_new.npy', P_bias_new)
#np.save('Q_bias_new.npy', Q_bias_new)

np.save('P_p.npy', P_pred)
np.save('Q_p.npy', Q_pred)
np.save('P_b.npy', P_bias)
np.save('Q_b.npy', Q_bias)
