from datetime import time
import os

def clear_screen():
    os.system('cls')
    
# 1 - Показать все записи +
# 2 - Найти запись по вхождению частей имени +
# 3 - Найти запись по телефону +
# 4 - Добавить новый контакт +
# 5 - Удалить контакт +
# 6 - Изменить номер телефона у контакта +
# 7 - Выход +

def save_lines(data):
    with open('book.txt', 'a', encoding='utf8') as datafile:
        data_to_save = ",".join(data) + "\n"
        datafile.write(data_to_save)
            
def print_lines(dataprint):
    while(True):
        for line in dataprint:
            print(",".join(line))
        answer = input("Enter для возврата в меню:>")
        if answer == "": return

def show_lines():
    result = []
    with open('book.txt', 'r', encoding='utf8') as datafile:
        for line in datafile:
            line = line.strip('\n')
            result.append(line.split(','))
        return result

def find_lines():
    while(True):
        show_me = []
        for line in show_lines():
            show_me.append(",".join(line))
        request = input("Запрос: ")
        show_me = list(filter(lambda line: request in line, show_me))
        show_me = show_me[0].split(",")
        print(f'Фамилия: {show_me[0]}\nИмя: {show_me[1]}\nОтчество: {show_me[2]}\nТелефон: {show_me[3]}')
        answer = input("Enter для возврата в меню:>")
        if answer == "": return

def add_lines():
    while (True):
            print('Добавление записи')
            last_name = input("Фамилия: ")
            first_name = input("Имя: ")
            patronymic = input("Отчество: ")
            phone_number = input("Номер телефона: ")
            data_to_save = [last_name, first_name, patronymic, phone_number]
            lets_out = input('(Enter - выход)')
            save_lines(data_to_save)
            if "" in lets_out: return


def remove_lines(): 
    while(True):
        show_me = []
        for line in show_lines():
            show_me.append(",".join(line))
        request = input("Кого удалим? (Введите часть контакта): ")
        show_me = list(filter(lambda line: request not in line, show_me))
        with open('book.txt', 'w', encoding='utf8') as datafile:
            for line in show_me:
                datafile.write(line+'\n')
        answer = input(f"Запись {request} удалена. Enter для возврата в меню:>")
        if answer == "": return
    

def change_lines():
     while(True):
        show_me = []
        for line in show_lines():
            show_me.append(",".join(line))
        request = input("Чей номер нужно обновить: ")
        update_number = []
        update_number = list(filter(lambda line: request in line, show_me))
        update_number = update_number[0].split(",")
        update_number[3] = (+input("Новый номер: "))
        show_me = list(filter(lambda line: request not in line, show_me))
        show_me.append(",".join(update_number))
        with open('book.txt', 'w', encoding='utf8') as datafile:
            for line in show_me:
                datafile.write(line+'\n')
        answer = input(f"Запись {request} обновлена. Enter для возврата в меню:>")
        if answer == "": return
       