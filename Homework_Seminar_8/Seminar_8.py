# Вычислить значение выражения:
# 12 + 15
# 12 / 15
# 112 * 15
# 1. Где операторы?
# 2. Где числовые значения?
# Уровень 1:
# - 1 действие
# - 2 аргумента
# Уровень 2:
# - Количество действие произвольное
# 12 + 15 - 4
# Уровень 3:
# - Действия имеют приоритет
# 12 - 4*2
# Уровень 4:
# - Действия разделяются скобками
# (12 - 4) * 2

# Решение

# n = '22 + 300'
# m = n.split()   #список
# print(m)

# a = int(m[0])
# c = m[1]
# b = int(m[2])
# print(a, b, c)

# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '/':
#     print(a / b)
# elif c == '*':
#     print(a * b)


#уровень 2

# n = '22 + 300 - 14 + 10 + 10'
# m = n.split()   #список
# print(m)

# def calc(a, b, ch):
#     if ch == '+':
#         return a + b
#     elif ch == '-':
#         return a - b
#     elif ch == '/':
#         return a / b
#     elif ch == '*':
#         return a * b

# a = int(m[0])
# c = m[1]
# b = int(m[2])

# print(a, b, c)
# print(calc(a, b, c))
# result = calc(a, b, c)

# for i in range(3, len(m) - 1, 2):
#     result = calc(result, int(m[i+1]), m[i])
#     print(m[i], m[i+1])
#     print(result)


# Уровень 3:
#     Действия имеют приоритет
# 12 - 4*2 +6/3

n = '22 * 300 - 14 + 10 * 10'

m = n.split()   #список
m2 = []
print(m)

def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b

result = int(m[0])


for i in range(1, len(m) - 1, 2):
    if m[i] == '*' or m[i] == '/':
        result = calc(int(m[i -1]), int(m[i+1]), m[i])
        m2.append(result)
    else:
        m2.append(m[i])
        m2.append(int(m[i+1]))


print(m[i], m[i+1])
print(m2)
print(result)

#дз доделать
n = '12 - 4 * 2 + 6 / 3'

def priority(example1: str) -> None:
    m = example1.split()
    m2 = []

    if m[0].isdigit():
        m.insert(0, '+')

    result = 0

    for i in range(0, len(m)-1, 2):
        if m[i] == '*':
            multyply = int(m2[-1]) * int(m[i+1])
            m2[-1] = multyply
        elif m[i] == '/':
            division = int(m2[-1]) / int(m[i+1])
            m2[-1] = division
        else:
            m2.append(m[i])
            m2.append(m[i+1])

    for i in range(0, len(m2)-1, 2):
        if m2[i] == '+':
            result += int(m2[i+1])
        elif m[i] == '-':
            result -= int(m2[i+1])
        else:
            continue
    print(example1 + ' = ' + str(result))

priority(n)


# Уровень 4 * (дополнительная задача, сдавать не обязательно)
#     Действия разделяются скобками
# (12 - 4) * 2 

n = '( 12 - 4 ) * 2 '     # примеры со скобками

def parenthesis(example2: str) -> None:                     
    arith_operations = {
            '+': (1, lambda x, y: x + y), 
            '-': (1, lambda x, y: x - y),
            '*': (2, lambda x, y: x * y), 
            '/': (2, lambda x, y: x / y)}

    digits_stack = []
    symbols_stack = []

    m = example2.split()

    for symbol in m:
        if symbol.isdigit():
            digits_stack.append(int(symbol))
        elif symbol in arith_operations:
            if len(symbols_stack) == 0:
                symbols_stack.append(symbol)
                continue
            if symbols_stack[-1] == '(':
                symbols_stack.append(symbol)
                continue

            while symbols_stack:
                if arith_operations.get(symbol)[0] < arith_operations.get(symbols_stack[-1])[0]:
                    y, x = digits_stack.pop(), digits_stack.pop()
                    digits_stack.append(arith_operations[symbols_stack[-1]][1](x, y))
                    del symbols_stack[-1]

                elif arith_operations.get(symbol)[0] == arith_operations.get(symbols_stack[-1])[0]:
                    y, x = digits_stack.pop(), digits_stack.pop()
                    digits_stack.append(arith_operations[symbols_stack[-1]][1](x, y))
                    del symbols_stack[-1]

                symbols_stack.append(symbol)
                break

        elif symbol == ')':
            while symbols_stack[-1] != '(':
                y, x = digits_stack.pop(), digits_stack.pop()
                digits_stack.append(arith_operations[symbols_stack[-1]][1](x, y))
                del symbols_stack[-1]
            if symbols_stack[-1] == '(':
                del symbols_stack[-1]
        else:
            symbols_stack.append(symbol)

    while len(symbols_stack) > 0:
        y, x = digits_stack.pop(), digits_stack.pop()
        digits_stack.append(arith_operations[symbols_stack[-1]][1](x, y))
        del symbols_stack[-1]

    result = digits_stack.pop()

    print(example2 + ' = ' + str(result))


parenthesis(n)