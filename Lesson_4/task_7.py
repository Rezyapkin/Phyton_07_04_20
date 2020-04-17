
# Задание 7, урок 4


def fibo_gen():
    result = 1
    val = 1
    while True:
        result *= val
        val += 1
        yield result


value = 1
for el in fibo_gen():
    print(f'{value}! = {el}')
    if value >= 15:
        break
    value += 1
