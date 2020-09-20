"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
    который должен принимать данные (список списков) для формирования матрицы.
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
    класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д."""
import random


class Matrix:
    def __init__(self, row, column):            # конструктор класса, принимающий кол-во строк и колонок матрицы
        self.row = row
        self.column = column
        self.matrix = [[random.randrange(10) for j in range(column)] for i in range(row)]   # генерир-е матрицы

    def __str__(self):                          # метод вывода матрицы
        return f'{self.matrix}'

    def __add__(self, other):                   # метод сложения матриц
        new_matrix = self.matrix                # присваивание 1-й матрицы
        for i in range(len(self.matrix)):               # обход индексов строк и колонок
            for j in range(len(self.matrix[i])):
                new_matrix[i][j] += other.matrix[i][j]      # прибавление элементов 2-й матрицы того же индекса
        return f'{new_matrix}'


matrix_one = Matrix(5, 5)
matrix_two = Matrix(5, 5)
print(matrix_one)
print(matrix_two)
print(matrix_two + matrix_one)