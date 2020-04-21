'''
Задание 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

input_file_name = 'task_4_in.txt'
output_file_name = 'task_4_out.txt'

en_dictionary = {'One': 'Один',
                 'Two': 'Два',
                 'Three': 'Три',
                 'Four': 'Четыре',
                 }

with open(input_file_name, 'rt', encoding='UTF-8') as input_file:
    with open(output_file_name, 'w', encoding='UTF-8') as output_file:
        for str_in_file in input_file:
            for key, value in en_dictionary.items():
                #Тут можно добавить условие на поиск ключа в строке
                str_in_file = str_in_file.replace(key, value)
            output_file.write(str_in_file)
