
# Задание 5, урок 2

my_list = [7, 5, 3, 3, 2]
print('Изначальный список: ', my_list)

while True:
    value = input('Введите натульное целое число: ')
    if value.isdigit():
        break
    print('Не верный ввод. Повторите попытку.')

value = int(value)

#Решение в лоб
index = 0
len_list = len(my_list)

while index < len_list:
    if value > my_list[index]:
        my_list.insert(index, value)
        break
    elif index == len_list-1:
        my_list.append(value)
    index += 1

print('Итоговый список: ', my_list)

#Для больших списков можно двоичную тихтомию использовать для ускорения