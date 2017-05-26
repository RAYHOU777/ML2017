
import scipy.io as sio
import sys
import numpy as np
import csv





def elu(arr):
    return np.where(arr > 0, arr, np.exp(arr) - 1)

def make_layer(in_size, out_size):
    w = np.random.normal(scale=0.5, size=(in_size, out_size))
    b = np.random.normal(scale=0.5, size=out_size)
    return (w, b)

def forward(inpd, layers):
    out = inpd
    for layer in layers:
        w, b = layer
        out = elu(np.dot(out,  w) + b)

    return out

def gen_data(dim, layer_dims, N):
    layers = []
    data = np.random.normal(size=(N, dim))

    nd = dim
    for d in layer_dims:
        layers.append(make_layer(nd, d))
        nd = d

    w, b = make_layer(nd, nd)
    gen_data = forward(data, layers)
    gen_data = np.dot(gen_data ,w) + b
    return gen_data

def get_eigenvalues(data):
    SAMPLE = 1 # sample some points to estimate
    NEIGHBOR = 200 # pick some neighbor to compute the eigenvalues
    randidx = np.random.permutation(data.shape[0])[:SAMPLE]
    knbrs = NearestNeighbors(n_neighbors=NEIGHBOR,
                             algorithm='ball_tree').fit(data)

    sing_vals = []
    for idx in randidx:
        dist, ind = knbrs.kneighbors(data[idx:idx+1])
        nbrs = data[ind[0,1:]]
        u, s, v = np.linalg.svd(nbrs - nbrs.mean(axis=0))
        s /= s.max()
        sing_vals.append(s)
    sing_vals = np.array(sing_vals).mean(axis=0)
    return sing_vals


def intrinsic_dimension(X, k1=6, k2=12, 
                        estimator='levina', metric='vector', 
                        trafo='var', mem_threshold=5000):

    n = X.shape[0]
    if estimator not in ['levina', 'mackay']:
        raise ValueError("Parameter 'estimator' must be 'levina' or 'mackay'.")
    if k1 < 1 or k2 < k1 or k2 >= n:
        raise ValueError("Invalid neighborhood: Please make sure that "
                         "0 < k1 <= k2 < n. (Got k1={} and k2={}).".
                         format(k1, k2))
    X = X.copy().astype(float)
        
    if metric == 'vector':
        # New array with unique rows   
        X = X[np.lexsort(np.fliplr(X).T)]
        
        if trafo is None:
            pass
        elif trafo == 'var':
            X -= X.mean(axis=0) # broadcast
            X /= X.var(axis=0) + 1e-7 # broadcast
        elif trafo == 'std':
            # Standardization
            X -= X.mean(axis=0) # broadcast
            X /= X.std(axis=0) + 1e-7 # broadcast
        else:
            raise ValueError("Transformation must be None, 'std', or 'var'.")
        
        # Compute matrix of log nearest neighbor distances
        X2 = (X**2).sum(1)
        
        if n <= mem_threshold: # speed-memory trade-off
            distance = X2.reshape(-1, 1) + X2 - 2*np.dot(X, X.T) #2x br.cast
            distance.sort(1)
            # Replace invalid values with a small number
            distance[distance<0] = 1e-7
            knnmatrix = .5 * np.log(distance[:, 1:k2+1])
        else:
            knnmatrix = np.zeros((n, k2))
            for i in range(n):
                distance = np.sort(X2[i] + X2 - 2 * np.dot(X, X[i, :]))
                # Replace invalid values with a small number
                distance[distance < 0] = 1e-7
                knnmatrix[i, :] = .5 * np.log(distance[1:k2+1])
    
    elif metric == 'distance':
        raise NotImplementedError("ID currently only supports vector data.")
        #=======================================================================
        # # TODO calculation WRONG
        # X.sort(1)
        # X[X < 0] = 1e-7
        # knnmatrix = np.log(X[:, 1:k2+1])
        #=======================================================================
    elif metric == 'similarity':
        raise NotImplementedError("ID currently only supports vector data.")
        #=======================================================================
        # # TODO calculation WRONG
        # print("WARNING: using similarity data may return "
        #       "undefined results.", file=sys.stderr)
        # X[X < 0] = 0
        # distance = 1 - (X / X.max())
        # knnmatrix = np.log(distance[:, 1:k2+1])
        #=======================================================================
    else:
        raise ValueError("Parameter 'metric' must be 'vector' or 'distance'.")
    
    # Compute the ML estimate
    S = np.cumsum(knnmatrix, 1)
    indexk = np.arange(k1, k2+1) # broadcasted afterwards
    dhat = -(indexk - 2) / (S[:, k1-1:k2] - knnmatrix[:, k1-1:k2] * indexk)
       
    if estimator == 'levina':  
        # Average over estimates and over values of k
        no_dims = dhat.mean()
    if estimator == 'mackay':
        # Average over inverses
        dhat **= -1
        dhat_k = dhat.mean(0)
        no_dims = (dhat_k ** -1).mean()
           
    return int(no_dims.round())
    
testfile      = sys.argv[1]
outfile       = sys.argv[2]

if __name__ == '__main__':

    ans=[]
    hid=[]
    for i in range(3):
        dim = np.random.randint(1,60)
        Nn = np.random.randint(1,10)*10000
        layer_dims = [np.random.randint(60, 80), 100]

        data = gen_data(dim, layer_dims, Nn)
        ans.append(dim)
        hid.append(layer_dims)

        print i



    ans_out = open(outfile, 'w')
    ans_out.write('SetId,LogDim' + '\n')


    N = 200
    loaddata = np.load(testfile)
    for i in range(N):

        load = loaddata[str(i)]  

        load = load[0:5000, ]
        #print load.shape

     #   m_dim = 100
     #   n_dim = 2000
        #VECT_DATA = np.random.rand(n_dim, m_dim)
        out_dim = intrinsic_dimension(load, 10, 20)


        if out_dim==21:
            out_dim = 55
        elif out_dim==20:
            out_dim = 45
        elif out_dim==19:
            out_dim = 40
        elif out_dim==18:
            out_dim = 35
        elif out_dim==17:
            out_dim = 30

        elif out_dim==16:
            out_dim = 25
        elif out_dim==15:
            out_dim = 20
        elif out_dim==14:
            out_dim = 15
        elif out_dim==13:
            out_dim = 10
        elif out_dim==12:
            out_dim = 5
        elif out_dim==1:
            out_dim = 2


        print ('nu %s = %s = %s' %(i, out_dim,np.log(out_dim)))
        #print ("==================================")

        ans_out.write(str(i) + ',' + str(np.log(out_dim)) + '\n')

'''
        if out_dim >16 and out_dim <=21:
            if out_dim==21:
                out_dim   = 59
            elif out_dim==20:
                out_dim   = 52
            elif out_dim==19:
                out_dim   = 45
            elif out_dim==18:
                out_dim   = 40
 
        elif out_dim <=16 and out_dim >=13:
            if out_dim==16:
                out_dim   = 30
            elif out_dim==15:
                out_dim   = 20
            elif out_dim==14:
                out_dim   = 10
            elif out_dim==13:
                out_dim   = 5

'''





