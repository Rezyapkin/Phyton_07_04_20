'''
Задание 5, урок 6.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:

    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self):
        self.title = 'Ручка'

    def draw(self):
        print('Пишем ручкой')


class Pencil(Stationery):

    def __init__(self):
        self.title = 'Карандаш'

    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):

    def __init__(self):
        self.title = 'Маркер'

    def draw(self):
        print('Пишем маркером на доске')


my_pen = Pen()
print(my_pen.title)
my_pen.draw()
print('-' * 30)

my_pencil = Pencil()
print(my_pencil.title)
my_pencil.draw()
print('-' * 30)

my_handle = Handle()
print(my_handle.title)
my_handle.draw()
print('-' * 30)
