# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random


try:
    n = int(input('Введите размер массива: '))
    x = int(input('Введите число X: '))
    list_1 = []
    for i in range(n):
        list_1.append(random.randint(1, n))
    print(*list_1, sep=" ")
    for i in list_1:
        if x == list_1[i]:
            print(list_1[i])

except:
    print('Ввод не совсем корректный. Попробуйте еще раз!')