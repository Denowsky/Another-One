

def WriteFile(file_name):
    with open(file_name, 'a') as data:
        data.writelines(input()+'\n')
        
def ReadFile(file_name):
    result = []
    with open(file_name, 'r') as data:
        for line in data:
            result.append(line.split())
    return result

def FindUsers(userList):
    name = 'Ivan,'
    for user in userList:
        if user[1] == name:
            print(user[3])

