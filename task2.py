"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
    К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
    параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
    для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""
from abc import ABC, abstractmethod


class Clothes(ABC):                 # базовый класс Одежда
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod                 # создание абстрактного метода
    def consumption(self):
        pass


class Coat(Clothes):                # класс Пальто
    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    def consumption(self):          # метод расчета расхода ткани для Пальто
        consumption_coat = self.__size / 6.5 + 0.5
        return consumption_coat


class Suit(Clothes):                # класс Костюм
    def __init__(self, name, height):
        super().__init__(name)
        self.__height = height

    def consumption(self):          # метод расчета расхода ткани для Пальто
        consumption_suit = 2 * self.__height + 0.3
        return consumption_suit


def print_consumption(res):
    print('Расход ткани для {}, составлет: {:.2f}'.format(res.name, res.consumption()))


coat1 = Coat('Пальто', 53)
suit1 = Suit('Костюм', 180)
print_consumption(coat1)
print_consumption(suit1)

"""Расчет общего расхода ткани"""
print('Общий расход ткани: {:.2f}'.format(coat1.consumption() + suit1.consumption()))