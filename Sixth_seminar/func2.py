from datetime import time
import os

def clear_screen():
    os.system('cls')
    
# 1 - Показать все записи +
# 2 - Найти запись по вхождению частей имени +
# 3 - Найти запись по телефону +
# 4 - Добавить новый контакт -
# 5 - Удалить контакт -
# 6 - Изменить номер телефона у контакта -
# 7 - Выход +
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

# def add_lines():
#     while (True):
#             print('Добавление записи("" - выход)')
#             last_name = input("Фамилия: ")
#             first_name = input("Имя: ")
#             patronymic = input("Отчество: ")
#             phone_number = input("Номер телефона: ")
#             data_to_save = [last_name, first_name, patronymic, phone_number]
#             if "" in data_to_save: return
#             (data_to_save)

# def remove_lines():


# def change_lines():

# print_lines(show_lines())