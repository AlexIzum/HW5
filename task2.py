# Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum_numbers(max1, min1):
    if min1 > 0:
        max1 = sum_numbers(max1 + 1, min1 - 1)
    return max1
a1 = int(input('Введите число 1: '))
b1 = int(input('Введите число 2: '))

print('Сумма этих чисел =', sum_numbers(max(a1, b1), min(a1, b1)))
