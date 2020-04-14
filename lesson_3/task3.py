
# Задание 3, урок 3

# Решение в 1 строку
def my_func_1(*args):
# Не судите строго, я реализовал для любого количества аргументов
    return sum(sorted(args)[-2:])

# Решение циклом
def my_func_2(*args):
    max_sum = 0
    for index, value in enumerate(args,1):
        current_sum = (value + max(args[index:])) if args[index:] else 0
        max_sum = current_sum if current_sum > max_sum else max_sum
    return max_sum

print(my_func_1(1, 3, 2))
print(my_func_2(1, 3, 2))