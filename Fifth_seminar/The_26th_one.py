# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
try:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))

    def MakePow(arg1,arg2):
        if arg2==1:
            return arg1
        else:
            return arg1*MakePow(arg1,arg2-1)
        
    print(MakePow(a,b))
except:
    print("Некорректный ввод")