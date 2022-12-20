# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

import random
n = int(input('Введите число монеток, лежащих на столе: '))
coinArray = []
count = 0
countHeads = 0
countTails = 0

# Сгенерируем случайное количество орлов и решек
for i in range(0, n):
    random_num = round(random.randint(0, 1))
    coinArray.append(random_num)


print(coinArray)
# Узнаем количество орлов и количество решек
for i in range(0, n):
    if coinArray[i] == 0:
        countTails += 1
    elif coinArray[i] == 1:
        countHeads += 1

# Переворачиваем монетки, которых менье
for i in range(0, n):
    if countTails > countHeads and coinArray[i] == 1:
        coinArray[i] = 0
    elif countTails < countHeads and coinArray[i] == 0:
        coinArray[i] = 1
           
print(f'Решка выпала {countTails} раз')
print(f'Орел выпал {countHeads} раз')

if countTails > countHeads:
    print(f'Минимальное количество монет, которые нужно перевернуть: {countHeads}')
else:
    print(f'Минимальное количество монет, которые нужно перевернуть: {countTails}')

print(coinArray)



