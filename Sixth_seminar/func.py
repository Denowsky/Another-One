from datetime import time
import os

def clear_screen():
    os.system('cls')
    
def search_data():
    clear_screen()
    while(True):
        answer = input('Строка поиска(\'\'-выход) :>')
        if answer == "": return
        result = []
        with open('book.txt', 'r', encoding='utf8') as datafile:
            for line in datafile:
                result.append(line.strip('\n'))
                print(result)
            result = list(filter(lambda line: answer in line, result))
        for printdata in result:
            output_data_string(printdata)
            
def output_data_string(printdata):
    parse_data = printdata.split(',')
    template = 'Фамилия: {0}\nИмя: {1}\nОтчество: {2}\nТелефон: {3}\n'
    print(template.format(parse_data[0], parse_data[1], parse_data[2], parse_data[3]))
    
def save_data_to_file(data_to_save):
    data_to_save = ",".join(data_to_save) + "\n"
    print(data_to_save)
    with open('book.txt', 'a', encoding='utf8') as datafile:
        datafile.write(data_to_save)
        
def print_data(enum=False):
    count = 0
    with open('book.txt', 'r', encoding='utf8') as datafile:
        for line in datafile:
            if enum:print(count + 1)
            output_data_string(line)
            count += 1
        return count
    
def print_all_data():
    count = print_data()
    input('Всего {} записей. Enter для выхода'.format(count))
    
def add_data():
    while (True):
        print('Добавление записи("" - выход)')
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone_number = input("Номер телефона: ")
        data_to_save = [last_name, first_name, patronymic, phone_number]
        if "" in data_to_save: return
        save_data_to_file(data_to_save)
        
def del_data():
    print("WIP")
        
def search_and_change():
    clear_screen()
    # answer = input('Строка поиска(\'\'-выход) :>')
    answer = 'Ivan'
    if answer == "": return
    result = []
    data_to_save = []
    with open('book.txt', 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n'))
        result = list(filter(lambda line: answer in line, result))
        for value in result[0].split(','):
            data_to_save.append(value)
        new_number = "+7921588123"
        if "" in new_number: return
        data_to_save[-1] = new_number
        print(data_to_save)
        save_data_to_file(data_to_save)
    
search_data()