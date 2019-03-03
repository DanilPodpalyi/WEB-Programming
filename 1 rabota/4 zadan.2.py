import math

a=[int(i) for i in input('Введите значения через пробел').split()]
y=a[1]
for i in range(len(a)): 
    if a[i]<y:
        y=int(a[i])

print ('y=',y)
