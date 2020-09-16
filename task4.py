"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
    speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
    которые должны сообщать, что машина поехала, остановилась, повернула (куда).
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
    свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    speed = 0
    color = 'red'
    name = 'monster'
    is_police = False

    def go(self, speed):
        if speed > 0:
            print('Машина поехала')

    def stop(self, speed):
        if speed == 0:
            print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self, speed):
        print(f'Скорость машины в данный момент: {speed}')


class TownCar(Car):
    def show_speed(self, speed):
        print(f'Скорость TownCar в данный момент: {speed}')
        if speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    color = 'yellow'


class WorkCar(Car):
    def show_speed(self, speed):
        print(f'Скорость WorkCar в данный момент: {speed}')
        if speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    is_police = True


car1 = TownCar()
print(car1.speed)
print(car1.color)
print(car1.name)
car1.go(10)
car1.show_speed(100)
car1.stop(10)
car1.turn('налево')
print(f'Это полицейская машина? {car1.is_police}', '\n')

car2 = SportCar()
print(car2.speed)
print(car2.color)
print(car2.name)
car2.go(70)
car2.show_speed(100)
car2.stop(0)
car2.turn('направо')
print(f'Это полицейская машина? {car2.is_police}', '\n')

car3 = WorkCar()
print(car3.speed)
print(car3.color)
print(car3.name)
car3.go(70)
car3.show_speed(50)
car3.stop(10)
car3.turn('налево')
print(f'Это полицейская машина? {car3.is_police}', '\n')

car4 = PoliceCar()
print(car4.speed)
print(car4.color)
print(car4.name)
car4.go(100)
car4.show_speed(100)
car4.stop(100)
car4.turn('налево')
print(f'Это полицейская машина? {car4.is_police}')