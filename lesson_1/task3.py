
# Задание 3

while True:
    n = input('Введите число n\n')
    if n.isdigit():
        result = int(n) + int(n*2) + int(n*3)
        print(f'Считаем: {n} + {n*2} + {n*3} = {result}')
    else:
        print('Введенное значение не является целым числом. Повторите ввод\n')