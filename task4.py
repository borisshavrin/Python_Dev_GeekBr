'''Программа принимает действительное положительное число x и целое отрицательное число y.
    Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
    функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
   Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.'''


def my_func(x, y):
    res = x ** y
    return res


def my_func2(x, y):
    i = 0
    res = 1
    while i > y:
        res /= x
        i -= 1
    return res


x = float(input('Введите действ. положительное число: '))
y = int(input('Введите целое отрицательное число: '))

print(my_func(x, y), my_func2(x, y))