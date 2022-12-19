# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
import random

size = 0
Num_list = []

while size<1:
    size = int(input("Сколько монет: "))
    if size>0:
        break
    print("Где деньги, Лебовски?)")
    
for num in range(0,size):
    random_number = int(round(random.uniform(0,1),0))
    Num_list.append(random_number)

def Find_Count(arg1):
    count = 0
    i = 0
    while i<len(arg1):
        if arg1[i]==0:
            count+=1
            i+=1
            continue # если число == 0, то цикл продолжается, но count+1
        i+=1
    Min = min(len(arg1)-count, count)
    print(len(arg1), end=" -> ")
    print(*arg1, sep=" ")
    print(Min)
    
Find_Count(Num_list)