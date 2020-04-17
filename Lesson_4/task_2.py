
# Задание 2, урок 4
import random

#Сгенерируем список со случайными элементами
random_list = [random.randint(0,100) for _ in range(10)]
print(f'Исходный список: {random_list}')

result_list = [value for index, value in enumerate(random_list) if index > 0 and value > random_list[index-1]]
print(f'Итоговый список: {result_list}')
