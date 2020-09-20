"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
    position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
    содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
    Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
    методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
    проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        inc = {'wage': wage, 'bonus': bonus}
        self._income = inc


class Position(Worker):                              # Класс на базе Worker
    def get_full_name(self):                         # метод получения полного имени сотрудника
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):        # метод получения дохода
        total_income = self._income['wage'] + self._income['bonus']
        return total_income


worker1 = Position('Николай', 'Леонтьев', 'Журналист', 50000, 15000)
name = worker1.get_full_name()
total_inc = worker1.get_total_income()
print(f'Зарплата сотрудника <{name}>, '
      f'находящегося должности <{worker1.position}>, составляет: {total_inc} р.')

worker2 = Position('Андрей', 'Смирнов', 'Администратор', 60000, 13000)
name = worker2.get_full_name()
total_inc = worker2.get_total_income()
print(f'Зарплата сотрудника <{name}>, '
      f'находящегося должности <{worker2.position}>, составляет: {total_inc} р.')