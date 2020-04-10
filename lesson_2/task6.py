
# Задание 6, урок 2

list_goods = []

'''
#Тестовый список
list_goods =[(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
             (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
             (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'}),
             ]
'''

good_code = 1

while True:

    good_name = input(f'Введите название товара №{good_code}\n')

    while True:
        good_price = input(f'Введите цену товара №{good_code}\n')
        try:
            good_price = float(good_price)
            break
        except:
            print('Вы ввели не верное значение. Повторите ввод')

    while True:
        good_count = input(f'Введите количество товара №{good_code}\n')
        try:
            good_count = float(good_count)
            break
        except:
            print('Вы ввели не верное значение. Повторите ввод')

    good_unit = input(f'Введите единицу измерения товара №{good_code}\n')

    new_dict = {'название': good_name,
                'цена': good_price,
                'количество': good_count,
                'eд': good_unit,
                }

    new_tupple = (good_code, new_dict)

    list_goods.append(new_tupple)

    good_code += 1

    print('Товаров в списке: ', len(list_goods))
    need_add = input('Добавить еще один товар в список? (Y/N)\n')
    if need_add.upper() != "Y":
        break


#Выведем получившися список с товарами
print('-'*30)
print(list_goods)
print('-'*30)

statistics_dict = {}

for good_code, tmp_tuple in list_goods:
    for key in tmp_tuple:
        if not key in statistics_dict:
            #Если в итоговом словаре нет такого ключа, то создаем его и пишем список с одним элементом
            statistics_dict[key] = [tmp_tuple[key]]
        elif not tmp_tuple[key] in statistics_dict[key]:
            #Если в значения такого нет, то добавляем. При отсутствии этого улсовия, значения повторялись бы
            statistics_dict[key].append(tmp_tuple[key])

print(statistics_dict)
