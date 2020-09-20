"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
    К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
    параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
    для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""
from abc import ABC


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @classmethod                    # создание абстрактного метода
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        consumption = self.param / 6.5 + 0.5
        return consumption


class Suit(Clothes):
    @property
    def consumption(self):
        consumption = 2 * self.param + 0.3
        return consumption


coat = Coat(100)
suit = Suit(180)

print('Расход ткани для пальто {}-го размера, составлет: {:.2f}'.format(coat.param, coat.consumption))
print('Расход ткани для костюма (рост {}см) составляет: {:.2f}'.format(suit.param, suit.consumption))

print('Общий подсчет расхода ткани: {:.2f}'.format(coat.consumption + suit.consumption))