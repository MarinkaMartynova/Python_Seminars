# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа 
# X и Y (X,Y ≤ 1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


def natNumbers():

    sum = int(input('Сумма чисел, загаданных Петей: '))
    s = sum
    prod = int(input('Произведение чисел, загаданных Петей: '))
    p = prod
    x = (s-int((s**2-4*p)**0.5))//2
    y = (s+int((s**2-4*p)**0.5))//2
    
    print(f'Первое натуральное число: {x}')
    print(f'Второе натуральное число: {y}')
    
natNumbers()