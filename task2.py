"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
    Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
    делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class Check(Exception):
    def __init__(self, number):
        self.number = number

    def __truediv__(self, other):
        try:
            if other.number == 0:
                raise Check("Введите знаменатель больше нуля")
        except Check as err:
            print(err)
        else:
            res = self.number / other.number
            return res


number1 = Check(int(input()))
number2 = Check(int(input()))
print(number1 / number2)