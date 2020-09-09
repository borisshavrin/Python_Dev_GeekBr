'''2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
      имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
      как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.'''

name = 'Alex'
surname = 'Smith'
birth = '14.03.2010'
city = 'NY'
email = 'alexsmith@gmail.com'
phone = '333-122-1444'


def user_d(name, surname, birth, city, email, phone):
    user_data = f'{name} {surname} {birth} {city} {email} {phone}'
    return user_data


print(user_d(name, surname, birth, city, email, phone))

