# Уровень 2:
# Количество действий произвольное
# 12 + 15 - 4

test = '12 + 15 - 4'
def MakeAction(data):
    splited = data.split(" ")
    return splited

def Calc(list_1):
    a = list_1[0]
    for i in range(1,len(list_1)-1,2):   
        match list_1[i]:
            case "+":
                a+=list_1[i+1]
            case "-":
                a-=list_1[i+1]
    print(*list_1, sep= " ", end="")
    return print(f' = {a}')
            
def Initial(list_1):
    for i in range(0, len(list_1),2):
        list_1[i]=int(list_1[i])
    return list_1

Calc(Initial(MakeAction(test)))