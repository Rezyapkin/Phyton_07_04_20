'''
Задание 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
import os

file_name = os.path.join(os.path.dirname(__file__), 'text.txt')

with open(file_name, 'wt', encoding='UTF-8') as file:
    my_str = '-'
    while my_str:
        my_str = input()
        file.write(my_str + '\n')
