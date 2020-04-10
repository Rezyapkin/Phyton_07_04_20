# Задание 5, урок 2

my_list = [7, 5, 3, 3, 2]
print('Изначальный список: ', my_list)

while True:
    value = input('Введите натульное целое число: ')
    if value.isdigit():
        break
    print('Не верный ввод. Повторите попытку.')

value = int(value)

# Решение в лоб
for index, element in enumerate(my_list, 0):
    if value > element:
        my_list.insert(index, value)
        break
    elif index == len(my_list) - 1:
        my_list.append(value)
        break

print('Итоговый список: ', my_list)

# Для больших списков можно двоичную тихтомию использовать для ускорения
