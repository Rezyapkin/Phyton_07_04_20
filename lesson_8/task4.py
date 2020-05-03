'''
Задание 4. Урок 8.
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
'''

from abc import ABC, abstractmethod

printing_technology = ('лазерная', 'струйная', 'матричная')
paper_sizes = ('А4', 'А3', 'А2', 'А1', 'А0')


class Warehouse:
    __stock = {}  # Остатки оргтехники на складе

    def __init__(self, address: str, square: float, capacity: float):
        """
        address - адрес находжения склада, square - площадь в м2, capacity - вместимость в м3
        """
        self.address = address
        self.square = square
        self.capacity = capacity


class Products:
    def __init__(self, name: str, paper_size: str, brand="", warranty=0):
        """
        :param name: наименование оргтехники
        :param paper_size: размер бумаги (одно из значений кортежа paper_sizes)
        :param brand: производитель
        :param warranty: гарантия в мес.
        """
        if not paper_size in paper_sizes:
            raise ValueError(f'Не верный формат бумаги. Должен принимать одно из значений: {paper_sizes}')
        self.name = name
        self.type = ""
        self.brand = brand
        self.warranty = warranty

    def __str__(self):
        return self.name


class Scaner(Products):
    def __init__(self, name: str, paper_size: str, brand="", warranty=0, scan_resolution=1200):
        """
        :param name: наименование товара
        :param paper_size: размер бумаги (одно из значений кортежа paper_sizes)
        :param brand: производитель
        :param warranty: гарантия в мес.
        :param scan_resolution: разрешение в dpi
        """
        super().__init__(name, paper_size, brand, warranty)
        self.type = "сканер"
        self.scan_resolution = scan_resolution


class Printer(Products):
    def __init__(self, name: str, paper_size, print_technology: str, brand="", warranty=0):
        """
        :param name: наименование товара
        :param paper_size: размер бумаги (одно из значений кортежа paper_sizes)
        :param brand: производитель
        :param warranty: гарантия в мес.
        :param print_technology: технология печати (одно из значений кортежа printing_technology)
        """
        super().__init__(name, paper_size, brand, warranty)
        self.type = "принтер"
        if print_technology in printing_technology:
            self.print_technology = print_technology
        else:
            raise ValueError(f'Технология печати должна принимать одно из значений: {printing_technology}')


class Xerox(Printer, Scaner):
    def __init__(self, name: str, paper_size, print_technology: str, brand="", warranty=0, scan_resolution=1200):
        """
        :param name: наименование товара
        :param paper_size: размер бумаги (одно из значений кортежа paper_sizes)
        :param brand: производитель
        :param warranty: гарантия в мес.
        :param print_technology: технология печати (одно из значений кортежа printing_technology)
        :param scan_resolution: разрешение сканера в dpi
        """
        super().__init__(name, paper_size, print_technology, brand, warranty)
        #Scaner.__init__(self, paper_size, brand, warranty, scan_resolution)
        self.type = "копировальное устройство"


my_xerox = Xerox('Копировальное устройство Xerox X1250', 'А4', 'лазерная', 'Xerox', 36)
print(my_xerox)
print(my_xerox.__dict__)
