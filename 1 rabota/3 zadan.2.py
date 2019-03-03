import math

a=[int(i) for i in input('Введите значения через пробел').split()]
y=0
for i in range(len(a)): 
    if (a[i]<11) and (a[i]>0):
        y=y+int(a[i])

print ('y=',y)

