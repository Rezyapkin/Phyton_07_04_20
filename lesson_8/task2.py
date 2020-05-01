'''
Задание 2. Урок 8.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class MyZeroDevisionException(Exception):
    def __init__(self, txt):
        self.txt = txt

# Я хотел подменить процедуру деления в классе float и там вызывать новую ошибку, но не получилось(((


while True:
    numerator = input('Введите числитель: ')
    denominator = input('Введите знаменатель: ')
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if not denominator:
            raise MyZeroDevisionException("Делить на 0 нельзя")
        result = numerator / denominator
        print(f'Результат: {result:.2f}')
    except ValueError:
        print('Не верный ввод.')
    except MyZeroDevisionException:
        print('Нельзя делить на 0')

    cont = input("Продолжить? (Y/N) ")
    if cont.upper() == "N":
        break
