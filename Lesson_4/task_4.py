
# Задание 4, урок 4

import random

#Сгенерируем список со случайными элементами
random_list = [random.randint(0, 10) for _ in range(20)]
print(f'Исходный список: {random_list}')

result_list = [value for value in random_list if random_list.count(value) == 1]
print(f'Итоговый список: {result_list}')
