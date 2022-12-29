# Задача 22:

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6

# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6

# 6 12

import random
n = int(input('Введите длину массива 1: '))
m = int(input('Введите длину массива 2: '))
array1 = []
array2 = []
count = 0

# заполняем массив случайными натуральными числами
for arr1 in range(0, n):
    random_number1 = round(random.randint(0, n))
    array1.append(random_number1)
print(array1)


for arr2 in range(0, m):
    random_number2 = round(random.randint(0, m))
    array2.append(random_number2)
print(array2)

array1.sort()
print(array1)
array2.sort()
print(array2)

res = set(array1) & set(array2)
if (len(res) > 0):
    print('совпадают: ', res)
else:
    print('нет совпадений')

