'''
Задание 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

file_name = 'text.txt'
with open(file_name, 'wt', encoding='UTF-8') as file:
    my_str = '-'
    while my_str:
        my_str = input()
        file.write(my_str + '\n')
