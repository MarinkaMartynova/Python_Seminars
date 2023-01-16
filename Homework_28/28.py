# Задача 28:

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.


def sum(a,b):
    return a if b == 0 else sum(a + 1, b -1) if b > 0 else sum(a - 1, b +1)

a,b = map(int, input().split())
print(sum(a,b))
