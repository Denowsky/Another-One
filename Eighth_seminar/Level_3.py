# Уровень 3:
# Действия имеют приоритет
# 12 - 4*2 +6/3

test = '12 - 4*2 + 6/3'
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
    return a
            
def Initial(list_1):
    for i in range(0, len(list_1),2):
        if '*' in list_1[i]:
            temp = list_1[i].split('*')
            list_1[i] = int(temp[0])*int(temp[1])
        elif '/' in list_1[i]:
            temp = list_1[i].split('/')
            list_1[i] = int(temp[0])/int(temp[1])
        list_1[i]=int(list_1[i])
    return list_1

print(f'{test} = {Calc(Initial(MakeAction(test)))}')