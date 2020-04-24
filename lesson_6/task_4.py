'''
Задание 4, урок 6.
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''
import random

class Car:

    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
         print('Машина поехала')
         self.speed = random.randint(30, 90)

    def stop(self):
         print('Машина остановилась')
         self.speed = 0

    def turn(self, direction):
         print(f'Машина повернула {direction}')

    def show_speed(self):
         print(f'Скорость машины: {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Внимание! Превышение скорости.')


class SportCar(Car):

    def go(self):
        print('Машина поехала')
        self.speed = random.randint(60, 200)


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Внимание! Превышение скорости.')


class PoliceCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True


car_1 = PoliceCar('хаки','Ford Focus')
print(f'{car_1.name} ({car_1.color}):')
car_1.go()
car_1.turn('на 180 градусов')
car_1.show_speed()
car_1.stop()
print('-' * 30)

car_2 = SportCar('красный','Lamporgini Urus')
print(f'{car_2.name} ({car_2.color}):')
car_2.go()
car_2.turn('резко')
car_2.show_speed()
car_2.stop()
print('-' * 30)

car_3 = WorkCar('белый','Газель')
print(f'{car_3.name} ({car_3.color}):')
car_3.go()
car_3.turn('направо')
car_3.show_speed()
car_3.stop()
print('-' * 30)

car_4 = TownCar('голубой','Renault Logan')
print(f'{car_4.name} ({car_4.color}):')
car_4.go()
car_4.turn('налево')
car_4.show_speed()
car_4.stop()
