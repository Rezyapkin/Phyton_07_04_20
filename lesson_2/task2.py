
# Задание №2, урок №2

test_list = []

while True:
    count = input('Введите количество элементов списка: ')
    if count.isdigit():
        count = int(count)
        break
    else:
        print('Вы ввели не верное значение. Повторите ввод')

while len(test_list) < count:
    test_list.append(input('Введите новый элемент списка: '))

print('Изначальный список: ',test_list)

for index in range(0,count-1,2):
    test_list[index], test_list[index+1] = test_list[index+1], test_list[index]

print('Итоговый список: ',test_list)
