# level 1 : разделяет операторы и аргументы 1.06
test = '12 - 15 + 12'
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
            case "*":
                a*=list_1[i+1]
            case "/":
                a/=list_1[i+1]
    print(*list_1, sep= " ", end="")
    return print(f' = {a}')
            
def Initial(list_1):
    for i in range(0, len(list_1),2):
        list_1[i]=int(list_1[i])
    return list_1

Calc(Initial(MakeAction(test)))
# level 2 : разделяет операторы и аргументы
# test_2 = '12 / 15'
# level 3 : определяет последовательность
# test_3 = '(12-4)*2'
# level 4 : 

