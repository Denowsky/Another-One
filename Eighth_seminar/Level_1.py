# Вычислить значение выражения
# Уровень 1:
# 1 действие
# 2 аргумента 12 + 15

test = '12 + 15'
def MakeAction(data):
    splited = data.split(" ")
    match splited[1]:
        case "+":
            return int(splited[0])+int(splited[2])
        case "-":
            return int(splited[0])-int(splited[2])
        case "*":
            return int(splited[0])*int(splited[2])
        case "/":
            return int(splited[0])/int(splited[2])

print(f'{test} = {MakeAction(test)}')