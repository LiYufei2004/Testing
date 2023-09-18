import numpy as np
a=[]
b=[]
while(1):
    temp=input()
    if(temp==''):
        break
    ad=temp.split()
    a.append(ad)
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        a[i][j]=int(a[i][j])
for j in range(0,len(a[0])):
    temp=input()
    ad=temp.split()
    b.append(ad)
for i in range(0,len(b)):
    for j in range(0,len(b[i])):
        b[i][j]=int(b[i][j])
na=np.array(a)
nb=np.array(b)
print("max_position of the first matrix: ",end='')
for i in na:
    print(np.argmax(i)+1,end=' ')
print()
print("max_position of the second matrix: ",end='')
for i in nb:
    print(np.argmax(i)+1,end=' ')
print()
nc=na@nb
for i in nc:
    for j in i:
        print(j,end=' ')
    print()
# print(na@nb)