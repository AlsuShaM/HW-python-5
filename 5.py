# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень 
# B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def f(a, b):
    if b == 0:
        return 1
    return f(a, b-1) * a

print(f(2, 3))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    return a

print(sum(2, 2))