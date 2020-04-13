
# Задание 2

time_in_sec = input('Введите время в секундах\n')

if time_in_sec.isdigit():
    #Верный ввод
    time_in_sec = int(time_in_sec)
    hours = time_in_sec // 3600
    minutes = (time_in_sec % 3600) // 60
    seconds = time_in_sec % 60
    print(f'Время в формате hh:mm:ss - {hours:>02}:{minutes:>02}:{seconds:>02}')
else:
    #Ввели не верно значение
    print('Введено не верно значение')
