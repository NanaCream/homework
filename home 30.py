# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1+ (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a_1 = int(input("Введите первое число арифм.прогрессии: "))
razn = int(input("Введите разность между элементами арифм.прогрессии: "))
count = int(input("Введите количество элементов арифм.прогрессии: "))
a_i = a_1
list_1 = [a_1]
for i in range (1,count):
    a_i= a_i+razn
    list_1.append(a_i)

print (* list_1)