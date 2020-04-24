'''
Задание 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json, os

input_file_name = os.path.join(os.path.dirname(__file__), 'task_7.txt')
out_file_name = os.path.join(os.path.dirname(__file__), 'task_7.json')
firms_dict = {}
profits = []

with open(input_file_name, 'rt', encoding='UTF-8') as file:
    for str_in_file in file:
        try:
            columns = str_in_file.split()
            profit = int(columns[2]) - int(columns[3])

            if profit > 0:
                profits.append(profit)

            firms_dict[columns[0]] = profit

        except Exception:
            print('Не верный формат файла')

output_list = [firms_dict, {'average_profit': int(sum(profits) / len(profits))}]
print(output_list)

with open(out_file_name, 'wt', encoding='UTF-8') as file:
    json.dump(output_list, file)