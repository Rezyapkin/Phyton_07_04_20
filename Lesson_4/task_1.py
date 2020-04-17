
# Задание 1, урок 4

from sys import argv

try:
    _, production, rate, bonus = argv
    production = int(production)
    rate = float(rate)
    bonus = float(bonus)
    result = (production * rate) + bonus
    print(f'Заработная плата сотрудника: {result}')

except ValueError:
    print('Не верные параметры вызова скрипта')
    print('1-й параматр - выработка в часах (int)')
    print('2-й параметр - ставка в час (float)')
    print('3-й параметр - премия (float)')
