
# Задание 4, урок 3

# Используем **
def my_func_1(x: float, y: int):
#Возводит x в отрицательную степень y, добавил, чтобы и в положительную
    return x ** y if y >= 0 else 1 / (x ** abs (y))


# Используем цикл
def my_func_2(x: float, y: int):
#Возводит x в отрицательную целую степень y
    result = 1
    for index in range(0, abs(y)):
        result /= x
    return result


# Используем рекурсию
def my_func_3(x: float, y: int):
#Возводит x в отрицательную целую степень y
    return my_func_3(x, y + 1) / x if y < 0 else 1


while True:
    x = input('Введите действительное положительно число x : ')
    try:
        x = float(x)
        break
    except ValueError:
        print('Вы ввели не верное значение. Повторите ввод')

while True:
    y = input('Введите целое отрицательное число y: ')
    try:
        y = int(y)
        if y >= 0:
            print('Вы ввели не отрицательное число. Повторите ввод')
        else:
            break
    except ValueError:
        print('Вы ввели не верное значение. Повторите ввод')

print(f'Результат работы функции 1: {my_func_1(x, y):.6f}')
print(f'Результат работы функции 2: {my_func_2(x, y):.6f}')
print(f'Результат работы функции 3: {my_func_3(x, y):.6f}')