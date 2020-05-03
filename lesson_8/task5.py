'''
Задание 5. Урок 8.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
'''
#Я специально "нагородил" хранение остатка товаров по Code, чтобы использовать classmethod для получения товара по Code

import datetime


printing_technology = ('лазерная', 'струйная', 'матричная')
paper_sizes = ('А4', 'А3', 'А2', 'А1', 'А0')


class Products:
    __code = 0 # код товара
    __dict_products = {} # словарь товаров

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
        Products.__code += 1
        self.__code = Products.__code
        Products.__dict_products[Products.__code] = self

    def __str__(self):
        return self.name

    @property
    def code(self):
        return self.__code

    @classmethod
    def get_product_by_code(cls, code):
        return cls.__dict_products.get(code)


class Warehouse:
    def __init__(self, address: str, square: float, capacity: float):
        """
        address - адрес находжения склада, square - площадь в м2, capacity - вместимость в м3
        """
        self.address = address
        self.square = square
        self.capacity = capacity
        self.__stock = {}  # Остатки оргтехники на складе
        self.__arrival = [] # Поступление товара на склад
        self.__shipment = [] # Отгрузки оргтехники со склада

    def receipt(self, product: Products, quantity: int):
        """
        :param product: экземпляр оргтехники
        :param quantity: количество штук
        :return: None
        """
        if quantity > 0:
            if not product.code in self.__stock.keys():
                self.__stock[product.code] = 0
            self.__stock[product.code] += quantity
            new_operation = {}
            new_operation['date'] = datetime.datetime.now()
            new_operation['product'] = product
            new_operation['quantity'] = quantity
            self.__arrival.append(new_operation)

        else:
            raise ValueError('Количество принимаемого товара должно быть больше 0')

    def get_product_stock(self, product: Products) -> int:
        """
        :param product: экземпляр оргтехники по которому нужно узнать остаток на складе
        :return: остаток товара на складе в штуках
        """
        result = self.__stock.get(product.code)
        return result if result else 0

    def get_stock(self) -> list:
        return [{'product_code': itm,
                 'product_name': str(Products.get_product_by_code(itm)),
                 'quantity': self.__stock[itm],
                 } for itm in self.__stock]

    def movement_product(self, product: Products, quantity: int, reciever: str):
        """
        :param product: перемещаемый продукт
        :param quantity: количество перемещаемых единиц
        :param reciever: куда перемещаем
        :return:
        """
        current_stock = self.get_product_stock(product)
        if quantity <= 0:
            raise ValueError('Количество передаваемого товара должно быть больше 0')
        elif quantity > current_stock:
            raise ValueError(f'Недостаточно товара {product} на складе для перемещения')
        else:
            new_operation = {}
            new_operation['date'] = datetime.datetime.now()
            new_operation['reciever'] = reciever
            new_operation['product'] = product
            new_operation['quantity'] = quantity
            self.__shipment.append(new_operation)
            self.__stock[product.code] -= quantity
            if not self.__stock[product.code]:
                del self.__stock[product.code]

    def get_arrival(self):
        return self.__arrival

    def get_shipment(self):
        return self.__shipment


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


my_xerox = Xerox('Копировальное устройство Xerox X1250', 'А3', 'лазерная', 'Xerox', 36)
print(my_xerox)
print(my_xerox.__dict__)

my_printer = Printer('Принтер Canon LBP-6200', 'А4', 'лазерная', 'Canon', 24)
print(my_printer)
print(my_printer.__dict__)

my_scaner = Scaner('Сканер HP ScanJet', 'А4', 'HP', 12)
print(my_scaner)
print(my_scaner.__dict__)


my_warehouse = Warehouse('Москва, ул. Скаладская', 78, 10)
my_warehouse.receipt(my_xerox, 2)
my_warehouse.receipt(my_printer, 5)
my_warehouse.receipt(my_scaner, 3)
my_warehouse.receipt(my_xerox, 7)

print(my_warehouse.get_product_stock(my_printer))
print(my_warehouse.get_stock())

my_warehouse.movement_product(my_xerox, 9, 'брак')
print(my_warehouse.get_stock())
