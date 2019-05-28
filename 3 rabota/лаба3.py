groupmates = [
    {
        "name": u"Данил",
        "group": "БАП1801",
        "age": 18,
        "marks": [4, 4, 5]
    },
    {
        "name": u"Александр",
        "group": "БАП1801",
        "age": 18,
        "marks": [3, 3, 3]
    },
    {
        "name": u"Иван",
        "group": "БАП1801",
        "age": 18,
        "marks": [3, 2, 2]
    },
    {
        "name": u"Егор",
        "group": "БАП1801",
        "age": 18,
        "marks": [5, 4, 5]
    }
]
def func(stud):
    z=float(input('Введите минимальный допустимый балл '))
    for s in stud:
        b=s["marks"]
        x=0
        for i in b:
            x=x+i
        x=x/len(b)
        if x>z:
            print(s["name"].ljust(15),s["group"].ljust(8),str(s["age"]).ljust(8), str(s["marks"]).ljust(20))
func(groupmates)        
    
