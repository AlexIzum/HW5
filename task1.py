#  Задача 1
#  Напишите программу, которая на вход принимает два числа A и B, 
#  и возводит число А в целую степень B с помощью рекурсии.
#  A = 3; B = 5 -> 243 (3⁵) 
#  A = 2; B = 3 -> 8

def degree_f(number, degree):
    if degree > 0:
        number *= number
        degree_f(number, degree - 1)
    if degree == 0:
        return 1
    return number


a = int(input('Введите число: '))
b = int(input('Введите степень: '))

print(f'{a}^{b} =', degree_f(a, b))