# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6

# -> 5

n=int(input("Введите число значений в массиве: "))
list_1=list()
ostanovka=0
#list_1= list ( i for i in range(1,n+1))   # массив A[1..N]
#Если массив вводить вручную пользователем:
for i in range(n):
    chislo_massiva=int(input("Введите число массива: "))
    list_1.append (chislo_massiva)


chislo = int(input("Введите число для сравнения: "))
sosed_min=list()
sosed_max=list()
for i in set(list_1):
    if i<chislo:
        sosed_min.append(i)
    elif i>chislo:
        sosed_max.append(i)
    elif i==chislo:
        print ("Число", chislo, "находится в массиве" )
        ostanovka=1
        break



if ostanovka==0:
    if sosed_min!=[] and sosed_max!=[]:
        if abs(chislo-max(sosed_min))<abs(min(sosed_max)-chislo):
            print ("Число", chislo, "находится между", max(sosed_min), "и", min(sosed_max), ", но ближе к :", max(sosed_min))
        else: 
            print ("Число", chislo, "находится между", max(sosed_min), "и", min(sosed_max), ", но ближе к :", min(sosed_max))

        if abs(chislo-max(sosed_min))==abs(min(sosed_max)-chislo):
            print ("Число", chislo, "равноудалено от", max(sosed_min), "и", min(sosed_max) )
    else:
        if sosed_min==[]:
            print ("Число", chislo, "ближе к :", min(sosed_max))
        elif sosed_max==[]:
            print ("Число", chislo, "ближе к :", max(sosed_min))

