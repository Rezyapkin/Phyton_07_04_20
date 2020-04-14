
# Задание 5, урок 3

total = 0
error = False

while not error:
    my_str = input('Введите строку состоящую из чисел : ')
    my_list = my_str.split(' ')
    sum_in_list = 0
    for number in my_list:
        try:
            sum_in_list += float(number)
        except ValueError:
            #Завершаем работу программы
            error = True
            break
    if sum_in_list or not error:
        #or not error добавил на тот случай, если пользователь ввел нули через пробелы
        total += sum_in_list
        print(f'Сумма чисел в этой строке: {sum_in_list:.2f}')
        print(f'Общая сумма введенных чисел: {total:.2f}')

