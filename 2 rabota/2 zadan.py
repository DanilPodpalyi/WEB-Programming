import math

a=[str(i) for i in input('Введите значения через пробел ').split()]
for i in range(len(a)): 
    if len(a[i])<10:
        print(a[i])

