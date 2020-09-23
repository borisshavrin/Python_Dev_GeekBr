class Cell:                                 # класс Клетка
    def __init__(self, qty):
        if type(qty) is not int:            # если количество ячеек клетки -не целое число, то возвращаем ошибку
            raise ValueError('Количество клеток должно быть целым числом')
        self.qty = qty

    def __add__(self, other):
        if type(other) is not Cell:     # если обьект не класса Клетка - возвращаем ошибку
            raise ValueError('Класс объекта должен быть - Клетка')
        sum_qty = self.qty + other.qty
        return Cell(sum_qty)

    def __sub__(self, other):
        if type(other) is not Cell:     # если обьект не класса Клетка - возвращаем ошибку
            raise ValueError('Класс объекта должен быть - Клетка')
        sub = self.qty - other.qty
        if sub < 0:
            raise ValueError('разность количества ячеек двух клеток меньше нуля')
        return Cell(sub)

    def __mul__(self, other):
        if type(other) is not Cell:     # если обьект не класса Клетка - возвращаем ошибку
            raise ValueError('Класс объекта должен быть - Клетка')
        mul = self.qty * other.qty
        return Cell(mul)

    def __truediv__(self, other):
        if type(other) is not Cell:     # если обьект не класса Клетка - возвращаем ошибку
            raise ValueError('Класс объекта должен быть - Клетка')
        truediv_qty = round(self.qty/other.qty)
        return Cell(truediv_qty)

    def make_order(self, row):
        n = self.qty // row                 # количество строк
        finish = self.qty % row             # остаток, который будем добавлять в конце
        line = ''
        for i in range(0, n):
            line += '*' * row + '\n'        # формируем целые строки
        if finish > 0:
            line += '*' * finish            # добавляем остаток
        return line


a = Cell(15)
b = Cell(12)
print(a.make_order(5))
print()
print(b.make_order(5))
print()

cell1 = a + b
cell2 = a - b
cell3 = a / b
print(cell3.qty)
print(cell1.make_order(5))