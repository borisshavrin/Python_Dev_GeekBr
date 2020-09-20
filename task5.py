"""Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка).
    Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
    В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов методы должен выводить уникальное сообщение.
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title

    def drow(self):
        print(f'Запуск отрисовки:')


class Pen(Stationery):
    def drow(self):
        super().drow()
        print(f'Сделайте надпись с помощью {self.title}')


class Pensil(Stationery):
    def drow(self):
        super().drow()
        print(f'Обведите контур, используя {self.title}')


class Handle(Stationery):
    def drow(self):
        super().drow()
        print(f'Выделите фрагмент с помощью {self.title}')


s1 = Pen('Ручка')
s1.drow()

s2 = Pensil('Карандаш')
s2.drow()

s3 = Handle('Маркер')
s3.drow()