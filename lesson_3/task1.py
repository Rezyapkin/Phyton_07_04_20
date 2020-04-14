# Задание 1, урок 3

def my_devision(numerator: float, denominator: float) -> float:
    # Выполняет деление двух чисел и отрабатывает ошибку на 0
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print('Ошибка деления на 0')


my_template = {'numerator': ('числитель', float),
               'denominator': ('знаменатель', float),
               }

my_input = {}

for key, values in my_template.items():
    while True:
        my_input[key] = input(f'Введите {values[0]}: ')
        try:
            my_input[key] = float(my_input[key])
            break
        except ValueError:
            print('Вы ввели не верное значение. Повторите ввод')

print(my_devision(my_input['numerator'], my_input['denominator']))
