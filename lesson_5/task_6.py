'''
Задание 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету
и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

import os

'''
Функция подсчитаетывает количество занятий определенного типа
Если они не найдены, функция возвращает 0
'''
def calc_sum(my_str: str):

    types_less = ('(л)', '(пр)', '(лаб)')
    for type_less in types_less:
        #Пытаемся отделить то что слева от типа, если он конечно есть
        new_str = my_str.split(type_less)
        #Если такой тип найден, то произойдет разделение и новая строка станет меньше
        if len(new_str[0]) < len(my_str):
            try:
                return int(new_str[0])
            except ValueError:
                return 0
    return 0


file_name = os.path.join(os.path.dirname(__file__), 'task_6.txt')
my_dict = {}

with open(file_name, 'rt', encoding='UTF-8') as file:
    for str_in_file in file:
        try:
            split_str = str_in_file.split(':')
            caption = split_str[0]
            #Расщепляем правую часть на слова
            words_in_right = split_str[1].split(' ')

            sum_in_str = sum(map(calc_sum, words_in_right))
            my_dict[caption] = sum_in_str

        except Exception:
            print('Не верный формат файла')

print(my_dict)
