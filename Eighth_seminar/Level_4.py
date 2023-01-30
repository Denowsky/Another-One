# Уровень 4 * (дополнительная задача, сдавать не обязательно)
# Действия разделяются скобками
# (12 - 4) * 2 

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
    for i in range(0, len(list_1),2):
        if '*' in list_1[i]:
            temp = list_1[i].split('*')
            list_1[i] = int(temp[0])*int(temp[1])
        elif '/' in list_1[i]:
            temp = list_1[i].split('/')
            list_1[i] = int(temp[0])/int(temp[1])
        list_1[i]=int(list_1[i])
    for j in range(1, len(list_1)-1,2):
        if list_1[j] == "*":
            list_1[j-1] = list_1[j-1]*list_1[j+1]
            list_1.pop(j)
            list_1.pop(j)
        elif list_1[j] == "/":
            list_1[j-1] = list_1[j-1]/list_1[j+1]
            list_1.pop(j)
            list_1.pop(j)  
    a = list_1[0]
    for i in range(1,len(list_1)-1,2):   
        match list_1[i]:
            case "+":
                a+=list_1[i+1]
            case "-":
                a-=list_1[i+1]
    return a
                   
print(f'{test} = {MakeAction(test)}')
