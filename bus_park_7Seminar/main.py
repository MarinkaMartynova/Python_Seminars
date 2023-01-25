import os
from menu import Menu
import function as fn

def clear_screen():      
    os.system("cls")

# if __name__ == "__main__":
#     #основной блок

menu_items = [
    ("1", "Вывод автобусов" ),
    ("2", "Добавление автобуса"),
    ("3", "Вывод водителей"),
    ("4", "Добавление водителей"),
    ("5", "Вывод маршрута"),
    ("6", "Добавление маршрута"),
    ("7", "Выход", lambda: exit())]

menu = Menu(menu_items)
# menu.run('Выберите необходимое действие: ')
for i in menu_items:
    print(i[0],i[1])

# print(menu_items)
text = input("Введите номер: ")

if text == '1':
    print(fn.print_bus())

elif text == '2':
    fn.add_bus()

elif text == '3':
    print(fn.print_driver())

elif text == '4':
    fn.add_driver()

elif text == '5':
    print(fn.print_route())

elif text == '6':
    fn.add_route()

elif text == '7':
    print("Спасибо, что воспользовались справочником маршрутов!")
    exit(0)