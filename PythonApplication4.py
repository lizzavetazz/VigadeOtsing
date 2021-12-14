from random import*

def arvud_loendis():
    """Andmete sisestus, funktsioonide kutsumine, vastust välja näitamine 
    """
    s=[]
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maksi)
    s=generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    neg=[]
    pos=[]
    null=[]
    pos,neg,null=jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos,n):
        lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg,n):
        lisamine(s,kesk):
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

arvud_loendis()


