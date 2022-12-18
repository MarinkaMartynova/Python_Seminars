# print('hello world')
#value = None           #пишем так, если в дальнейшем используем таую переменную
#a = 123
#b = 1.23
#print(type(a))         #type-нужен для идентификации типа значения
#print(type(b))
#value = 12334
#print(type(value))
#s = 'hello world'     #объявляем строку
#print(s)              #вывод строки

#s = "hello 'world"     #одинарная ковычка
#print(s)

#s = 'hello "world'     #двойная ковычка
#print(s)

#s = 'hello \'world'     #прописываем одну ковычку иным способом
#print(s)

#s = 'hello \nworld'     #переход на новую строку
#print(s)

#print(a, b, s)              
#print(a,' - ', b,' - ', s)               #способы вывода
#print('{} - {} - {}'.format(a, b, s))
#print(f'{a} - {b} - {s}')
#print('{1} - {2} - {0}'.format(a, b, s))   #чтобы поменять порядок

#логическая переменная
#f = True
#print(f)

#массивы

#list = ['1', '2', '3', 'hello', 1,2,3,5, True]
#print(list)
#пробел может поломать программу - синтаксис

# print() - отвечает за вывод данных
# input() - отвечает за ввод данных

#print('Введите а')
#a = int(input())   #если надо найти целое число
#print('Введите b')
#b = float(input())  #если значение дробное (через точку 1.2)
#print(a, ' + ', b, ' = ', a+b)
#print('{} {}'.format(a, b))
#print(f'{a} {b}')

#арифметические операции
# +, -, *, /, %, //, **
# (), сокращенные операции
# a = 2
# b = 8
# c = a+b
# d = a-b
# e = a*b
# f = b/a  #так деление записывается 4.0
# f = b//a #это если мы хотим остаток целый увидеть
# g = a%b
# print( c, ' ',d, ' ', e, ' ', f, ' ', g)

# a = 2.1323
# b = 8
# c = round(a*b, 5) #округление до 5 знаков
# print( c)


#сокращеные операции присваивания
# a = 3
# a += 5       # ==    a = a + 5
# print(a)

# закомментировать участок Ctrl + K + C
# расскомментировать участок Ctrl + K + U


#логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путатть с &,|,^
# и еще: is, is not, in, not in

# a = 1 > 3
# a = 1 < 4 and 5 > 2
# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# func = 1
# T = 4
# x = 123

# print(func<T>x)

#f = 1 > 2 or 4 < 6
#print(f)

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)

# Управляющие конструкиции: if, if-else

#if condition:
    # operator 1
    # operator 2

    # operator n

#else:
    # operator n + 1
    # operator n + 2

    # operator n + m


# a = int( input('a = '))
# b = int( input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)



#if condition1:
    # operator
#elif condition2:
    # operator
#elif condition3:
    # operator
#else:
    # operator


# username = input('Введите ваше имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Джон':
#     print('Джон -  топ')
# else:
#     print('Привет. '. username)

#Цикл while

#while condition:
    # operator 1
    # operator 2

    # operator n

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

#Цикл while-else

#while condition:
    # operator 1
    # operator 2

    # operator n

#else:
    # operator n + 1
    # operator n + 2

    # operator n + m


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй ')
#     print('хватит )')
# print(inverted)

#Цикл for

#for i in enumeration:
    # operator 1
    # operator 2

    # operator n

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1,5):
#     print(i)

# for i in range(1,10,2):    #третьим аргументом приращение, в результате получим нечетные числа
#     print(i)

# for i in 'qwer - ty':      #можно и строки записать и перечислить списком
#     print(i)

#немного о строках

# text = 'съешь еще этих мягких французких булок'  #если мы определили строку
# print(len(text))          # 39      мы легко можем узнать количество символов в строке, через функцию len
# print('еще' in text)      # True    если хотим проверить наличие какой-то подстроки - используем операто in
# print(text.isdigit())     # False   можно проверить являются ли все символы в строке числами
# print(text.islower())     # True    можно проверить являются ли все символы в строке символами нижнего регистра
# print(text.replace('еще', 'ЕЩЁ'))    #        если мы что-то хотим изменить
# for c in text:
#     print(c)

# если мы не знаем что делает како-то конкретный оператор , это можно узнать с помощью функции хелп
# text = 'съешь еще этих мягких французких булок'

# help(text.istitle)


# так называемые срезы
# text = 'съешь еще этих мягких французких булок'
# print(text[0])                 # с
# print(text[1])                 # ъ
# # print(text[len(text)])         # IndexError
# print(text[len(text) - 1])     # к
# print(text[-5])                # б
# print(text[:])                 # print(text)
# print(text[0:2])               # съ
# print(text[len(text) - 2:])    # ок
# print(text[2:9])               # ешь еще
# print(text[6:-18])             # еще этих мягких
# print(text[0:len(text):6])     # сеикакл
# print(text[::6])               # сеикакл

# Списки:введение
# Список - пронумерованная, изменяемая коллекция объектов (произвольных) типов

# numbers = [1, 2, 3, 4, 5]
# print(numbers)              # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)      # это приведение типа ранж к типу лист
# print(type(numbers))

# # numbers = list(range(1, 6))
# # print(numbers)              # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(f'{len(numbers)} len')            # [10, 2, 3, 4, 5]
# print(numbers)

# for i in numbers:
#     i *= 2              # обратить внимание: что этим действием мы в текущее значение кладем новое значение, не в список
#     print(i)                # [20, 4, 6, 8, 10]
#     print(numbers)                # [10, 2, 3, 4, 5]

#расширенный функционал, если хотим добавить какой то элемент то мы спокойно это делаем
# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)          # red, green, blue

# for e in colors:
#     print(e*2)    # redred, greengreen, blueblue

# colors.append('gray')    # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])  # True
# colors.remove('red') # del colors[0] удалить элемент

#  Функции. Описание
# это фрагмент программы, используемый многократно

# def function_name(x):     # def потом имя_аргумента (аргумент)
#     body line 1

#     body line n
#     optional return     #оператор возвращения


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))