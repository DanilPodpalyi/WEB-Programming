a=input('Введите строку ')
s=[]
y=[]
for i in range(len(a)):
    y=a[i]
    if y.isalpha():
        s=s+[a[i]]
print (s)


