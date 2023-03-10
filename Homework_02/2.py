# Задача 2
# Найдите сумму цифр трехзначного числа.

# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# вариант 1
# num = input("Введите трехзначное число: ")
# n = int(num)

# i1 = n % 10             # остаток от деления на 10 числа дает последнюю цифру числа.
# i2 = n % 100 // 10      # разделить полученное двухзначное число нацело на 10, и у нас окажется вторая цифра числа.
# i3 = n // 100           # Если исходное трехзначное число разделить нацело на 100, то получится первая цифра числа.

# print("Сумма цифр числа:", i1 + i2 + i3)



# вариант 2
# num = input("Введите трехзначное число: ")

# i1 = int(num[0])    # Извлекается первый[0] символ строки, преобразуется к целому. 
# i2 = int(num[1])    # Аналогично второй[1]
# i3 = int(num[2])    # Аналогично третий[2].

# print("Сумма цифр числа: ", i1 + i2 + i3)


# вариант преподавателя:
while True:
    try:
        num = int(input('Введите трехзначное число: '))
        if 99 < num and num < 1000:
            print(f'Сумма цифр: {num // 100 + num // 10 % 10 + num % 10}')
            break
        else:
            print('Это не трехзначное число. Попробуйте еще раз! :)')
    except:
        print('Некорректный ввод. Попробуйте еще раз!')
    