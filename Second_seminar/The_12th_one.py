# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа. 
# 4 4 -> 2 2
# 5 6 -> 2 3

# import random
# x1=int(round(random.uniform(0,1000),0))
# y2=int(round(random.uniform(0,1000),0))
# print(x1, y2)
# s=x1+y2
# p=x1*y2
s = 15
p = 50
print(f'{s} {p} ->', end=" ")
d = abs(s*s-4*p)
x = int((s+abs(d))/2)
y = int((s-abs(d))/2)
print(x, y)

