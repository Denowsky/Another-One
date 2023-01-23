
import func2

if __name__ == '__main__':
    menu = '''1 - Показать все записи\n2 - Найти запись по имени, фамилии, отчеству или телефону\n3 - Добавить новый контакт\n4 - Удалить контакт\n5 - Изменить номер телефона у контакта\n6 - Выход'''
    while (True):
        func2.clear_screen()
        print(menu)
        answer = input('>:')
        match answer:
            case "1":
                func2.print_lines(func2.show_lines())
            case "2":
                func2.find_lines()          
            case "3":
                func2.add_lines()
            case "4":
                func2.remove_lines()
            case "5":
                func2.change_lines()
            case "6":
                exit(0)
            case _:
                print("неверный ввод")
                func2.time.sleep(3)
            