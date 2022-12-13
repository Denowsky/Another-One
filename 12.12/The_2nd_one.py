# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

#methods
def Find_Sum_Of_Num(arg1):
    sum = 0
    count = 0
    if not arg1.isdigit() or len(arg1) != 3: # проверяем ввод по условию не текст и не длинее/короче 3хзначности
        print("Воу, нужно трёзначное число, повтори попытку")
        return
    else:
        while count<len(arg1): # цикл разбивания str со входа на цифры, перевод их в int и создание суммы
            temp = int(arg1[count])
            sum += temp
            count+=1
    print(f'{arg1} -> {sum} ({first_num[0]} + {first_num[1]} + {first_num[2]})')

#end of methods

first_num = input('Введите трёхзначное число: ')
Find_Sum_Of_Num(first_num)
