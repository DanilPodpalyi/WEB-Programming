import math

a=[str(i) for i in input('Введите значения через пробел ').split()]
y=0
for i in range(len(a)): 
    if (i+1)%2==0:
        print ('y=',a[i])
