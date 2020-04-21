'''
Задание 2 урок 5
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

file_name = "my_text.txt"

with open(file_name, 'rt', encoding='UTF-8') as file:
    count = 0
    for read_str in file:
        count += 1
        words_in_str = read_str.split(" ")
        print(f'В строке №{count} кол-во слова: {len(words_in_str)}')
    print(f'Количество строк в файле: {count}')
