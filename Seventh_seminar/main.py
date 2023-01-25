
import functions as func

if __name__ == '__main__':
    menu = '''1 - Вывод водителей\n2 - Добавление водителя\n3 - Вывод автобусов\n4 - Добавление автобуса\n5 - Вывод маршрутов\n6 - Добавление маршрута\n7 - Выход'''
    while (True):
        func.clear_screen()
        print(menu)
        answer = input('>:')
        match answer:
            case "1":
                func.print_lines(func.print_drivers())
            case "2":
                func.add_driver()          
            case "3":
                func.print_lines(func.print_busses())
            case "4":
                func.add_bus()
            case "5":
                func.show_route(func.print_routes(func.print_busses(), func.print_drivers()))
            case "6":
                func.add_route()
            case "7":
                exit(0)
            case _:
                print("неверный ввод")
                func.time.sleep(3)
            