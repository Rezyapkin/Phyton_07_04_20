
# Задание 5, урок 4

from functools import reduce

my_list = [value for value in range(100, 1001) if not value & 1]
print(my_list)

result = reduce(lambda x, y: x * y, my_list)
print(result)
