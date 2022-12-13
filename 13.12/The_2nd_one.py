# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

#methods
def Find_Sum_Of_Num(arg1):
    sum = 0
    count = 0
    if len(arg1) != 3:
        print("Воу, нужно трёзначное число, повтори попытку")
        return
    else:
        while count<len(arg1):
            temp = int(arg1[count])
            sum += temp
            count+=1
    print(f'{arg1} -> {sum} ({first_num[0]} + {first_num[1]} + {first_num[2]})') # в C# было бы проще вывести цифры в цикле по индексу count, а не по (0,1,2), так как там разделен вывод Write и WriteLine

#end of methods

first_num = input('Введите трёхзначное число: ')
Find_Sum_Of_Num(first_num)
