# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

#methods
def Find_Lucky_Ticket(arg1):
    sum_One = 0
    sum_Two = 0
    count = 0
    if len(arg1) != 6:
        print("Воу, нужно шестизначное число, повтори попытку")
        return
    else:
        while count<len(arg1)-3:
            temp = int(arg1[count])
            sum_One += temp
            count+=1
        while count<len(arg1):
            temp = int(arg1[count])
            sum_Two += temp
            count+=1
    if sum_One == sum_Two:
        print(f'{arg1} -> yes')
    else:
        print(f'{arg1} -> no')

def Reserv_Method(arg1):
    temp = arg1
    sum_one = 0
    sum_two = 0
    while temp>0:
        sum_one+= int(temp%10)
        temp=int(temp/10)
        print(sum_one)
    print(temp)
    temp = arg1
    while temp>0:
        sum_one+= int(temp%10)
        temp=int(temp/10)
        print(sum_one)
#end of methods

first_num = int(input('Введите шестизначное число: '))
# Find_Lucky_Ticket(first_num)
Reserv_Method(first_num)
