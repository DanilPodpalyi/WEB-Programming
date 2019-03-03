import math
def funk (a,b,c,d,k):
    z=abs(((a**2-b**3-(c**3)*(a**2))*(b-c+c*(k-d/(b**3)))-(k/b-k/a)*c)**2-20000)
    return z

a=int(input("Введите значение a "))
b=int(input("Введите значение b "))
c=int(input("Введите значение c "))
d=int(input("Введите значение d "))
k=int(input("Введите значение k "))
if (a==0) or (b==0):
    print("деление на 0")
else:
    z=funk(a,b,c,d,k)
    print(z)
