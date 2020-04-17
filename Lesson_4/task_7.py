
# Задание 7, урок 4


def fibo_gen(n):
    result = 1
    for item in range(1, n + 1):
        result *= item
        yield result


value = 1
for el in fibo_gen(15):
    print(f'{value}! = {el}')
    value += 1
