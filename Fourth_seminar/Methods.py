import random


def ListAppend(list, size):
    for i in range(size):
        list.append(random.randint(1, size))
    print(*list, sep=' ')


def CheckRepeat(arg1, arg2):
    result = []
    for i in set(arg1):
        for j in set(arg2):
            if j == i:
                result.append(j)
    if bool(result) is False:
        print("Нет совпадений")
    else:
        print(*result, sep=' ')


def FindMaxRow(arg1):
    max_sum = 0
    sum = 0
    for bush in arg1:
        sum = arg1[bush-1]+arg1[bush-2]+arg1[bush-3]
        if sum > max_sum:
            max_sum = sum
    print(max_sum)
