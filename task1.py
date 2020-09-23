"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
    который должен принимать данные (список списков) для формирования матрицы.
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
    класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д."""
import random


class Matrix:
    def __init__(self, list_numbers):
        self.matrix = list_numbers

    def __str__(self):                          # метод перевода матрицы в текстовый формат
        str_matrix = ''                         # создание пустой строки для внесения в нее чисел
        for i in self.matrix:
            for j in i:
                str_matrix += str('{:<4}'.format(j))     # перевод ряда матрицы в текст (c выравниванием)
            str_matrix += '\n'                  # перенос ряда на новую строку
        return str_matrix

    def __add__(self, other):                   # метод сложения матриц
        new_matrix = self.matrix                # присваивание 1-й матрицы
        for i in range(len(self.matrix)):               # обход индексов строк и колонок
            for j in range(len(self.matrix[i])):
                new_matrix[i][j] += other.matrix[i][j]  # прибавление элементов остальных матриц того же индекса
        return Matrix(new_matrix)


matrix_one = [[random.randrange(10) for j in range(5)] for i in range(3)]
matrix_two = [[random.randrange(10) for k in range(5)] for l in range(3)]
# matrix_three = [[random.randrange(10) for n in range(5)] for m in range(3)]
# matrix_four = [[random.randrange(10) for p in range(5)] for o in range(3)]

a = Matrix(matrix_one)
b = Matrix(matrix_two)
# c = Matrix(matrix_three)
# d = Matrix(matrix_four)

print(a)
print(b)
# print(c)
# print(d)
print(a + b)    # также работает с 3-4мя матрицами
