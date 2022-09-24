# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

import random

def get_list(row, column):
    numbers = []
    for i in range(row):
        numbers.append([random.randint(0, 30) for _ in range(column)])
    return numbers

def sort_list(mas):
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            for k in range(len(mas)):
                for l in range(len(mas[i])):
                    if mas[i][j] < mas[k][l]:
                        temp = mas[i][j]
                        mas[i][j] = mas[k][l]
                        mas[k][l] = temp
    return mas

try:
    my_row = int(input('Количество строк: '))
    my_column = int(input('Количество столбцов: '))
    my_list = get_list(my_row, my_column)
    print(my_list)
    print(sort_list(my_list))
except:
    print('Ошибка, нужно вводить целые числа')