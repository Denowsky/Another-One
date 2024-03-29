# Задачи на повторение по материалам предыдущих семинаров (по желанию)
# Задача 101 Вычислить число π c заданной точностью d
# Пример: 
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001
# import math,random
# try:
#     d = float(input("Введите точность d: "))
#     if d<0.00000000001 or d>0.1:
#         exit()
#     else:
#         count = 0
#         print(d)
#         while d<1:
#             d=d*10
#             count+=1
#         p = round(math.pi,count)
#         print(p)
# except:
#     print("Точность введена не точно")

# Задача 102 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# try:
#     n = int(input("Введите натуральное число N: "))
#     if n<0:
#         exit()
#     list = []
#     m = 2
#     while n>1:
#         if n%m!=0:
#             m+=1
#         else:
#             list.append(m)
#             n/=m
#     print(list)
# except:
#     print("N не подходит условиям")

# Задача 103 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.
# Пример:  k=2 
# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0 
# x*x + 5 = 0 
# 10*x*x = 0

# data = open('file1.txt', 'w')
# def ListAppend(list, size):
#     for i in range(size):
#         list.append(random.randint(0, size))


# Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена (
    # полученные в результате работы программы из задачи 103). Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.

# Задача 105 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Задача 106 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)

candies = 100
def take(sweets):
    while sweets>0:
        a = int(input('Введите число от 1 до 28: '))
        if a<=28 and a>0:    
            sweets = sweets-a
            print(sweets)
        else:
            if a<=0:
                print("Конфеты, дружище, бери конфеты")
            else:
                print("Куда столько? Возьми меньше.")
    return


candies = take(candies)
        

# Задача 107 Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)

# Задача 108 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (модуль в отдельном файле, импортируется как библиотека)
# метод Упаковка: на вход подается текстовый файл, на выходе текстовый файл со сжатием.
# метод Распаковка: на вход подается сжатый текстовый файл, на выходе текстовый файл восстановленный.
# Прикинуть достигаемую степень сжатия (отношение количества байт сжатого к исходному).