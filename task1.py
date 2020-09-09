'''Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''
from sys import argv

script_name, hours, cash, bonus = argv


def pay(hours, cash, bonus):
    hours = int(hours)
    cash = int(cash)
    bonus = int(bonus)
    res = (hours * cash) + bonus
    return res


print(pay(hours, cash, bonus))