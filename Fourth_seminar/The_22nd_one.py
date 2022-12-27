# Задача 22:  
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12
import random
def ListAppend(list, size):
    for i in range(size):
        list.append(random.randint(1, size))
def CheckRepeat(arg1,arg2):
    print(arg1)
    print(arg2)
    result = []
    for i in set(arg1):
        for j in set(arg2):
            if j==i:
                result.append(j)
    print(result)
                
list_1 = []
list_2 = []
n = int(input('Введите кол-во элементов первого набора: '))
m = int(input('Введите кол-во элементов второго набора: '))
ListAppend(list_1,n)
ListAppend(list_2,m)
CheckRepeat(list_1,list_2)