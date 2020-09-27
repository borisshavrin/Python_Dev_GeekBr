"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
    «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
    должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
    @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
     Проверить работу полученной структуры на реальных данных."""


class Data:
    def __init__(self, date):
        Data.date_str = date

    @classmethod
    def number(cls):
        number_date = cls.date_str.split('-')
        day = int(number_date[0])
        month = int(number_date[1])
        year = int(number_date[2])
        return '{:>4}: {} \n{:>4}: {} \n{}: {}'.format(day, type(day), month, type(month), year, type(year))

    @staticmethod
    def validation(date):
        number_date = date.split('-')
        day = int(number_date[0])
        month = int(number_date[1])
        year = int(number_date[2])
        if day not in range(1, 32):
            raise ValueError("Дней в месяце может быть от 1 до 31")
        if month not in range(1, 13):
            raise ValueError("Месяцев в году может быть от 1 до 12")
        if year not in range(2021):
            raise ValueError("Этот год еще не наступил")


date1 = '01-05-2020'
date2 = '32-13-2021'
print(Data(date1).number(), '\n')
print(Data.date_str)
print(Data.validation(date2))