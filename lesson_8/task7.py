"""
Задание 7. Урок 8.
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real: float, imag: float = 0):
        self.real = real
        self.imag = imag

    def __str__(self):
        result = str(self.real)
        if self.imag:
            imag_str = f'{str(abs(self.imag))}j'
            if self.real:
                result = " ".join([result,'+' if self.imag > 0 else '-',imag_str])
            else:
                result = "".join(['' if self.imag > 0 else '-',imag_str])
        return result

    def __add__(self, other):
        if type(other) == type(self):
            imag = self.imag + other.imag
            real = self.real + other.real
        elif type(other) in (float, int):
            imag = self.imag
            real = self.real + other
        else:
            raise TypeError(f'Неверный тип: {type(other)}')
        return Complex(real, imag)

    def __mul__(self, other):
        if type(other) == type(self):
            real =  self.real * other.real - (self.imag * other.imag)
            imag = self.imag * other.real + self.real * other.imag
        elif type(other) in (float, int):
            imag = self.imag * other
            real = self.real * other
        else:
            raise TypeError(f'Неверный тип: {type(other)}')
        return Complex(real, imag)

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    def __sub__(self, other):
        return Complex(self.__add__(-other))


print(f'({Complex(1.1, 1)}) + {1} = {Complex(1.1, 1) + 1}')
print(f'({Complex(2.1, 3.2)}) + ({Complex(0.3, -1)}) = {Complex(2.1, 3.2) + Complex(0.3, -1)}')
print(f'({Complex(2, 3)}) * ({Complex(5, 4)}) = {Complex(2, 3) * Complex(5, 4)}')
print(f'- ({Complex(2.1, 3.2)}) = {- Complex(2.1, 3.2)}')
print(f'({Complex(2.1, 1.2)}) - ({Complex(2.1, 3.2)}) = {Complex(2.1, 1.2) -Complex(2.1, 3.2)}')
