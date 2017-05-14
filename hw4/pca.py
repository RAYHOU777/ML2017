

import numpy as np
from numpy.linalg import svd , eig
from scipy import misc
from PIL import Image
import matplotlib.pyplot as plt
cmap = plt.get_cmap('gray')
n=5
image=[]

nn = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

img_ls = []
for alp in nn:
	for i in range(10):
		idx = str(alp)+str(0)+str(i)
		filename = './data/%s.bmp' % idx
		image1 = misc.imread(filename, flatten= 0)
		image.append(image1)
image = np.array(image)
imagex = np.reshape(image,(100,64*64))

mean = np.mean(imagex,axis=0)
print(mean.shape)
imagec = (imagex-mean)
misc.imsave('mean.jpg', np.reshape(mean,(64,64)))
im=plt.imshow(np.reshape(mean,(64,64)),cmap=cmap)


print(imagec.shape)
U, s, V = svd(imagec, full_matrices=False)
#print(s.shape)
#imp = np.argsort(s)
#imp = imp[::-1]
new_s = s[range(n)]
new_U = U.T[range(n)].T
new_V = V[range(n)]



margin=1
m=3
w=64*m+(m-1)*margin
h=w
bm = np.zeros((h,w))
for j in range(m):
    for k in range(m):
        face_V=np.array([V[m*j+k]])
        eface = np.reshape(face_V,(64,64))
        bm[(64+margin)*j:(64+margin)*j+64,(64+margin)*k:(64+margin)*k+64]=eface
misc.imsave('eface.jpg', bm)        
im=plt.imshow(bm,cmap=cmap)
#plt.show()

margin=1
m=10
w=64*m+(m-1)*margin
h=w
bm = np.zeros((h,w))
for j in range(m):
    for k in range(m):
        face_V=np.array([image[m*j+k]])
        bm[(64+margin)*j:(64+margin)*j+64,(64+margin)*k:(64+margin)*k+64]=face_V
misc.imsave('ori.jpg', bm)        
im=plt.imshow(bm,cmap=cmap)
#plt.show()

image_new = np.dot(new_U,(np.dot(np.diag(new_s),new_V)))
image_new =  np.reshape(image_new,(100,64,64))+np.reshape(mean,(64,64))
margin=1
m=10
w=64*m+(m-1)*margin
h=w
bm = np.zeros((h,w))
for j in range(m):
    for k in range(m):
        face_V=np.array([image_new[m*j+k]])
        bm[(64+margin)*j:(64+margin)*j+64,(64+margin)*k:(64+margin)*k+64]=face_V
misc.imsave('new.jpg', bm)        
im=plt.imshow(bm,cmap=cmap)
#plt.show()





for i in range(1,101):
    new_s = s[range(i)]
    new_U = U.T[range(i)].T
    new_V = V[range(i)]
    image_new = np.dot(new_U,(np.dot(np.diag(new_s),new_V)))
    image_new =  np.reshape(image_new,(100,64,64))+np.reshape(mean,(1,64,64))
    perr = np.sum((image-image_new)**2)/i/64/64
    err = np.sqrt(perr)/256
    print(err)
    if err < 0.01:
    	break
print(i)   




















