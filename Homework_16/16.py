# Задача 16:

# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2


import random
n = int(input('Введите длину массива: '))
x = int(input('Введите число в массиве A, которое нужно проверить: '))
array = []
count = 0

# заполняем массив случайными натуральными числами
for num in range(1, n):
    random_number = round(random.randint(1, n//2))
    array.append(random_number)
print(array)

# находим, сколько раз число Х повторяется в массиве( условие диапозон элементов массива в 2 раза меньше длины его)
for i in range(1, n//2):
    i == x
    count +=1
print(f'Число {x} встречается: {array.count(x)} раз')



