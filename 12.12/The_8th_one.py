# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника). / на первый взгляд ничего не понятно, я предпочитаю батончики)
# Пример:
# 3 2 4 -> yes 
# 3 2 1 -> no
n = int(input('Введите число n: '))
m = int(input('Введите число m: '))
k = int(input('Введите число k: '))
if k%n==0 or k%m==0: # проверка на кратность: если собираемся отломить количество долек, кратное ширине или длинне шоколадки, то шоколадка отломится по прямой
    print(f'{n} {m} {k} -> yes')
else: 
    print(f'{n} {m} {k} -> no')