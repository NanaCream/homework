# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

n=int(input("Введите число значений в массиве: "))
list_1=list()
#list_1= list ( i for i in range(1,n+1))   # массив A[1..N]
#Если массив вводить вручную пользователем:
for i in range(n):
    chislo_massiva=int(input("Введите число массива: "))
    list_1.append (chislo_massiva)

count=0

chislo=int(input("Какое число мы ищем в массиве: ")) #Число х

for i in list_1:
    if i==chislo:
        count+=1
print("Загаданное число в массиве встречается - ", count, "раз")