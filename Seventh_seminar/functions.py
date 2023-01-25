from datetime import time
import os
from random import randint

def clear_screen():
    os.system('clear') # ноутбук с linux - я в командировке)

def print_lines(dataprint):
    while(True):
        for line in dataprint:
            print(",".join(line))
        answer = input("Enter для возврата в меню:>")
        if answer == "": return
                      
def print_drivers():
    result = []
    with open('crew.txt', 'r', encoding='utf8') as datafile:
        for line in datafile:
            line = line.strip('\n')
            result.append(line.split(','))
        return result
    
def add_driver():
    count = 0
    while(True):
        with open('crew.txt', 'r+', encoding='utf8') as datafile:
            answer = input("Enter - вернуться или Введите имя(англ): ")
            if answer == "": return
            else:
                for line in datafile:
                    count+=1
                datafile.write(f'\ndriver_{count+1}, {answer}')

def print_busses():
    result = []
    with open('vehicles.txt', 'r', encoding='utf8') as datafile:
        for line in datafile:
            line = line.strip('\n')
            result.append(line.split(','))
        return result
    
def add_bus():
    count = 0
    while(True):
        with open('vehicles.txt', 'r+', encoding='utf8') as datafile:
            answer = input("Enter - вернуться или Введите марку автобуса(англ): ")
            number = input("Введите номер автобуса(прим. u999rt66): ")
            if answer == "": return
            else:
                for line in datafile:
                    count+=1
                datafile.write(f'\nbus{count+1}, {number}, {answer}')
                
def print_routes(bus, driver):
    result = []
    with open('route.txt', 'r', encoding='utf8') as datafile:
        for line in datafile:
            line = line.strip('\n')
            result.append(line.split(','))
        for i in result:
            for j in bus:
                if i[2].strip(" ") == j[0]:
                    i[2] = ",".join(j)
            for k in driver:
                if i[3].strip(" ") == k[0]:
                    i[3] = ",".join(k)
        return(result)
    
def show_route(route):
     while(True):
        for line in route:
            print(f'номер маршрута: {line[0].strip(" ")}\nномер рейса: {line[1].strip(" ")}\nавтобус: {line[2].strip(" ")}\nводитель: {line[3].strip(" ")}\n')
        answer = input("Enter для возврата в меню:>")
        if answer == "": return   
    
def add_route():
    count = 0
    while(True):
        with open('route.txt', 'r+', encoding='utf8') as datafile:
            answer = input("Enter - вернуться или Введите рейсовый номер: ")
            number = input("Введите данные автобуса(Id): ")
            driver = input("Введите данные водителя(Id): ")
            if answer == "": return
            else:
                for line in datafile:
                    count+=1
                datafile.write(f'\nm{count+1}, {answer}, {number}, {driver}')
                