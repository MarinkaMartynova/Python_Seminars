import os
import time

file_name = 'pb.txt'

def clear_screen():      
    os.system("cls")    # для Windows  очистка экрана

def search_data():       # ввод нужного значения для поиска
    clear_screen()
    while True:
        answer = input("Введите параметр для поиска (фамилия/имя/отчество/номер телефона) (Еnter - выход) >:")
        if answer == "":
            return
        result = search_in_file(answer)
        for printdata in result:
            output_data_string(printdata)
        print("Всего найдено записей: {} \n".format(len(result)))


def search_in_file(request):
    result = []
    with open(file_name, "r", encoding="utf8") as datafile:
        for line in datafile:
            result.append(line.strip("\n"))
        result = list(filter(lambda line: request in line, result))
    return result


def output_data_string(printdata):
    parse_data = printdata.split(",")
    template = "{0:<30} Тел.: {1:<13}"
    print(template.format(parse_data[0]+' '+ parse_data[1]+' '+parse_data[2], parse_data[3]))


def save_data_to_file(data_to_save):
    # data_to_save = ",".join(data_to_save) + "\n"
    print(data_to_save)
    with open(file_name, "a", encoding="utf8") as datafile:
        datafile.write("\n")
        datafile.write(data_to_save)


def print_data():
    count = 0
    with open(file_name, "r", encoding="utf8") as datafile:
        for line in datafile:
            count += 1
            print(":{:<3} ".format(count), end=' ')
            output_data_string(line.strip('\n'))
    return count


def print_all_data():
    clear_screen()
    count = print_data()
    input("Всего {} Записей. Enter для выхода".format(count))


def add_data():
    clear_screen()
    while True:
        print('Добавление записи (Enter - выход) >:')
        last_name = input("Фамилия: ")
        if last_name == "":
            return
        first_name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone_number = input("Номер Телефона: ")
        data_to_save = [last_name, first_name, patronymic, phone_number]
        if "" in data_to_save:
            return
        save_data_to_file(data_to_save)


def del_data():
    while True:
        clear_screen()
        print("1 - удаление по порядковому номеру записи\n"
              "2 - удаление по параметру(значению)\n"
              "3 - выход")
        answer = input(">:").upper()
        match answer:
            case "1":
                del_data_by_number()
            case "2":
                del_data_by_search()
            case "3":
                return
            case _:
                print("неверный ввод")
                time.sleep(1)


def del_data_by_number():
    while True:
        clear_screen()
        print_data()
        answer = input("Введите номер записи для удаления(Q - выход)>: ")
        if answer.upper() == "Q":
            return
        if not answer.isnumeric():
            continue
        answer = int(answer)
        print(answer)
        phonedata = ""
        count = 0
        with open(file_name, "r", encoding="utf8") as datafile:
            for line in datafile:
                count += 1
                if answer == count:
                    continue
                phonedata += line

        with open(file_name, "w", encoding="utf8") as datafile:
            datafile.write(phonedata)


def del_data_by_search():
    clear_screen()
    while True:
        answer = input("Введите параметр для удаления(''-выход):")
        if answer == "":
            return
        found_records = search_in_file(answer)
        if len(found_records) == 0:
            print("нет записей для удаления")
        else:
            print("найдены записи: ")
            for printdata in found_records:
                output_data_string(printdata)
            if input('удаляем [Y-да/..-нет]').upper() == "Y":
                phonedata = ""
                with open(file_name, "r", encoding="utf8") as datafile:
                    for line in datafile:
                        if answer in line:
                            continue
                        phonedata += line

                with open(file_name, "w", encoding="utf8") as datafile:
                    datafile.write(phonedata)



if __name__ == "__main__":
    # основной блок
    clear_screen()
    menu = (f"Добро пожаловать в телефонный справочник!\n"
            "Главное меню\n"
            "1 - Вывод данных\n"
            "2 - Добавление записи\n"
            "3 - Поиск\n"
            "4 - Удаление записи\n"
            "5 - Выход\n")
    while True:
        clear_screen()
        print(menu)
        answer = input("->: ").upper()
        match answer:
            case "1":
                # вывод данных
                print_all_data()

            case "2":
                # добавление данных
                add_data()

            case "3":
                # поиск
                search_data()

            case "4":
                # удаление данных
                del_data()

            case "5":
                # выход
                print("Спасибо, что воспользовались справочником!")
                exit(0)

            case _:
                print("неверный ввод")
                time.sleep(1)
