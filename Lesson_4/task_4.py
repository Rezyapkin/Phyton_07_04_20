
# Задание 4, урок 4

import random

#Сгенерируем список со случайными элементами
random_list = [random.randint(0, 10) for _ in range(20)]
print(f'Исходный список: {random_list}')

result_list = [value for index, value in enumerate(random_list) if not value in random_list[:index]]
print(f'Итоговый список: {result_list}')
