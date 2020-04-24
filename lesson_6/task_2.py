'''
Задание 2, урок 6.
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self, weight_asphalt, thickness):
        return self._length * self._width * weight_asphalt * thickness


try:
    new_length = float(input('Введите длину дороги в метрах: '))
    new_width = float(input('Введите ширину дороги в метрах: '))

    new_weight_asphalt = float(input('Введите вес асфальта необходимый для покарытия 0,01 м3 дороги в кг: '))
    new_thickness = float(input('Введите требуюемую ширину дорожного покрытия в см: '))

    new_road = Road(new_length, new_width)
    print(f'Необходимо {new_road.calc_weight(new_weight_asphalt, new_thickness)/1000:.2f} тонн асфальта')

except ValueError:
    print('Вы ввели не верное значение!')
