"""Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
    реализуйте перегрузку методов сложения и умножения комплексных чисел.
    Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
    умножение созданных экземпляров. Проверьте корректность полученного результата."""


class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = complex(self.x, self.y)

    def __add__(self, other):
        sum_z = self.z
        sum_z += other.z
        return sum_z

    def __mul__(self, other):
        mul_z = self.z
        mul_z *= other.z
        return mul_z


num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(2, 2)

print(num1 + num2)
print(num1 * num2)