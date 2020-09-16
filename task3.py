"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
    position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
    содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
    Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
    методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
    проверить значения атрибутов, вызвать методы экземпляров)."""
inc = {}


class Worker:                                   # Базовый класс
    name = ''                                   # Атрибуты
    surname = ''
    position = ''
    _income = inc


class Position(Worker):                             # Класс на базе Worker

    def get_full_name(self, name, surname):         # метод получения полного имени сотрудника
        Worker.name = name
        Worker.surname = surname
        full_name = f'{name} {surname}'
        return full_name

    def get_total_income(self, wage, bonus):        # метод получения дохода
        Worker._income['wage'] = wage
        Worker._income['bonus'] = bonus
        total_income = wage + bonus
        return total_income


worker1 = Position()
print(worker1.get_full_name('Николай', 'Леонтьев'))
print(worker1.get_total_income(50000, 15000))

worker2 = Position()
print(worker2.get_full_name('Андрей', 'Смирнов'))
print(worker2.get_total_income(60000, 13000))

print(f'Словарь с последними данными: {inc}')
print(f'Атрибуты класса Worker: {Worker.name}, {Worker.surname}')
