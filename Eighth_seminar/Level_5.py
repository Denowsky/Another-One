# 

test = '(12 - 4) * 2'
def MakeAction(data):
    pos_first = 0
    pos_second = 0
    count = 0
    result = []
    for i in data:
        count+=1
        if i == '(':
            pos_first = count
        elif i == ')':
            pos_second = count
    result = data[pos_first:pos_second-1]
    result = MakeOperation(result)
    data = MakeOperation(data.replace(data[pos_first-1:pos_second],str(result)))
    return data

def MakeOperation(list_1):
    list_1 = list_1.split(" ")
    a = int(list_1[0])
    for i in range(1,len(list_1)-1,2):   
        match list_1[i]:
            case "*":
                a*=int(list_1[i+1])
            case "/":
                a/=int(list_1[i+1])
            case "+":
                a+=int(list_1[i+1])
            case "-":
                a-=int(list_1[i+1])
    return a
                   
print(f'{test} = {MakeAction(test)}')
