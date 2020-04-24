'''
Задание 1, урок 6.
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.
'''


import time

#Не до конца понял задание, но надеюсь сделал верно!
class TrafficLight:
    __traffic_colors = (('красный', 'желтый', 'зеленый'),
                        (7, 2, 10),
                        )
    __color = __traffic_colors[0][-1]

    def running(self, color):
        colors = TrafficLight.__traffic_colors[0]
        next_index_color = (colors.index(self.__color) + 1) % len(colors)
        if color not in colors:
            print(f'Светофор не может переключиться на {color} цвет')
        elif colors.index(color) == next_index_color:
            self.__color = color
            print(color)
            time.sleep(TrafficLight.__traffic_colors[1][next_index_color])
        else:
            print(f'После цвета {self.__color} должен идти {colors[next_index_color]} цвет, а не {color}')


my_light = TrafficLight()
my_light.running('красный')
my_light.running('желтый')
my_light.running('зеленый')
my_light.running('бурый')
my_light.running('красный')
my_light.running('зеленый')

