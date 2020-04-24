'''
Задание 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

# В файле фамилии и з/п специально введены с лишними пробелами

import os

file_name = os.path.join(os.path.dirname(__file__), 'file_task3.txt')

with open(file_name, 'rt', encoding='UTF-8') as file:
    lines = file.readlines()

    try:
        values = list(map(lambda value: float(value.replace(' ','')), lines[1::2]))

        print('-' * 30)
        for staff in lines[::2]:
            print(staff.strip())
        print('-' * 30)

        print(f'Средний заработок: {sum(values)/len(values):.2f}')

    except ValueError:
        print('Ошибочный формат файла')
