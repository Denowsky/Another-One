# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1  /Катя посередине, значит)
# 24 -> 4 16 4
# 60 -> 10 40 10

S = int(input('Введите число: '))
if S%2:
    print('По условию задачи число должно быть чётное')
else:
    One_Guy = int(S/3/2) #всего ребят трое, и вдвоём парни сделали в два раза меньше, чем Катя
    Kate = int(One_Guy*4) # Катя сделала в 4 раза больше, чем один из парней
    print(f'{S} -> {One_Guy} {Kate} {One_Guy}')