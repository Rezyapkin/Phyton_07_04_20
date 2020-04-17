
# Задание 6, урок 4

from itertools import count, cycle
from time import sleep
from random import randint

def generator_1(start: int):
    for value in count(start):
        print(value)
        sleep(0.5)


def generator_2(list):
    for value in cycle(list):
        print(value)
        sleep(0.5)

random_list = [randint(0, 100) for _ in range(10)]

#generator_1(10)
generator_2(random_list)
