
# Задание 4

while True:
    number = input('Введите целое неотрицательное число \n')
    if number.isdigit():
        temp_number = int(number)
        max_digi = 0
        while temp_number > 0:
            tmp = temp_number % 10
            max_digi = max(max_digi, tmp)
            if max_digi == 9:
                break
            temp_number //= 10
        print(f'Самая большая цифра в числе {number} - {max_digi}')
        break
    else:
        print('5Введенное значение не является целым неотрицательным числом. Повторите ввод\n')
