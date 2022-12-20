# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k),
# не превосходящие числа N.

# 5
# 1 2 4

# 17
# 1 2 4 8 16

# вариант попроще
# number = int(input('Введите число: '))
# i = 1
# print(1)
# while (2 * i) <= number:
#     print(2 * i)
#     i *= 2


# вариант через функцию def
def powerOfTwo(number):
    i = 1
    print('целые степени двойки: ')
    print(1)
    while (2 * i) <= number:
        print(2 * i)
        i *= 2
    
number = int(input('Введите число: '))
powerOfTwo(number)

