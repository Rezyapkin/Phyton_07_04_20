'''
Задание 2. Урок 7.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

class Clothes:
    expenditure = 0

    def __init__(self, name: str):
        self.name = name


class Coat(Clothes):
    def __init__(self, size: float):
        super().__init__("Пальто")
        self.size = size
        Clothes.expenditure += self.expenditure

    @property
    def expenditure(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height: float):
        super().__init__("Костюм")
        self.heigth = height
        Clothes.expenditure += self.expenditure

    @property
    def expenditure(self):
        return self.heigth * 2 + 0.3


while True:
    what_clothes = input("Что хотите сшить? (П - пальто), (К - костюм), (Иначе - выход) ? ")
    try:
        if what_clothes == "П":
            size = input("Какого размера? ")
            new_clothes = Coat(float(size))
        elif what_clothes == "К":
            height = input("На какой рост шьем? ")
            new_clothes = Suit(float(height))
        else:
            break
    except ValueError:
        print("Ошибка ввода.")
    print(f'Расход ткани: {new_clothes.expenditure:.2f}')

print(f'Общий расход ткани: {Clothes.expenditure:.2f}')
