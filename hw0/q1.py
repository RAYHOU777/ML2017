import numpy as np
import sys




file = open(sys.argv[1],'r')


lst1 = []
lst1= file.readline()
lst1a = lst1.split(',')
lst1aa = []
for ele in lst1a:
    lst1aa.append(int(ele.strip('\n')))
file.close()
x = np.array(lst1)
#print (lst1)
#print (lst1a)
#print (lst1aa)
file = open(sys.argv[2],'r')
lt1 = []
lt1= file.readline()
lt1a = lt1.split(',')
lt1aa = []
for ele1 in lt1a:
    lt1aa.append(int(ele1.strip('\n')))
file.close()

lists=[]

i=0
while i < len(lt1aa) :

    file = open(sys.argv[2],'r')
    lst2 = []
    lst2 = [line.split(",")[i] for line in file]
    file.close()
    lst2a=[]

    for elel in lst2:
       lst2a.append(int(elel))
#lst2a =int(lst2)
    y= np.array([lst2a])
#print y
#x1=str(x)
#y1=str(y.T)
#print y
    c=np.dot(lst1aa,lst2a)
    b=str(c)
    lists.insert(i,b)
   # print b
   # print lists
   # print i
    i+=1

cc = sorted(lists)
#print cc
file =open("ans_one.txt",'w')
print cc
for line in cc:
   file.write(line)
   file.write('\n')
file.close()


