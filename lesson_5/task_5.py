'''
Задание 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

import random

file_name = 'task_5.txt'

values = [random.randint(0, 1000) for _ in range(random.randint(1, 100))]
print(f'Сумма элементов списка: {sum(values)}')

with open(file_name, 'wt', encoding='UTF-8') as file:
    for value in values:
        #Тренарный добавил, чтобы пробел в конец или начало не попадал. Сэкономил байт)))
        file.write((' ' if file.tell() else '') + str(value))

with open(file_name, 'rt', encoding='UTF-8') as file:
    my_str = file.read()
    read_values_sum = sum(map(lambda in_str: int(in_str), my_str.split()))
    print(f'Сумма, прочитанная из файла: {read_values_sum}')