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
    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_polise

    def go(self):
        if self.speed > 0:
            print(f'{self.color} машина {self.name} поехала')
        else:
            self.stop()

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')
        else:
            self.go()

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} в данный момент: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super(TownCar, self).show_speed()
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60} км/ч')


class SportCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WorkCar(Car):
    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40} км/ч')


class PoliceCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_police = True


car1 = TownCar(100, 'Красная', 'Ford Focus', False)
car1.go()
car1.show_speed()
car1.stop()
car1.turn('налево')
print(f'Это полицейская машина? {car1.is_police}', '\n', '________________________', '\n')

car2 = WorkCar(100, 'Серая', 'Mercedes Sprinter', False)
car2.go()
car2.show_speed()
car2.turn('направо')
print(f'Это полицейская машина? {car2.is_police}', '\n', '________________________', '\n')

car3 = PoliceCar(100, 'Синяя', 'Audi A5', None)
car3.go()
car3.show_speed()
car3.turn('направо')
print(f'Это полицейская машина? {car3.is_police}', '\n', '________________________', '\n')

car4 = SportCar(0, 'Желтая', 'Nissan GTR', False)
car4.go()
car4.show_speed()
print(f'Это полицейская машина? {car4.is_police}', '\n', '________________________', '\n')