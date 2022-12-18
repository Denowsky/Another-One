# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа. // Что мы должны сделать?
# 44 -> 22

# X = None
# Y = None

import random

X = int(round(random.uniform(0,1000),0))
Y = int(round(random.uniform(0,1000),0))

S = X+Y
P = X*Y
print(f'Сумма = {S}, а произведение = {P}, какое число я загадал?')