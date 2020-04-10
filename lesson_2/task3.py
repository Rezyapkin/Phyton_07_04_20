
# Задание 3, урок 2

#Список для решения через список, хотя я бы решал через целочисленное деление
list_month = ['зима',
              'зима',
              'весна',
              'весна',
              'весна',
              'лето',
              'лето',
              'лето',
              'осень',
              'осень',
              'осень',
              'зима',
              ]

dict_month = {1: 'зима',
              2: 'зима',
              3: 'весна',
              4: 'весна',
              5: 'весна',
              6: 'лето',
              7: 'лето',
              8: 'лето',
              9: 'осень',
              10: 'осень',
              11: 'осень',
              12: 'зима',
              }

while True:
    month = input('Введите номер месяца: ')
    if month.isdigit():
        month = int(month)
        if month > 0 and month <= 12:
           break
    print('Введено не верное значение. Повторите ввод.')

 #Мой способ
print('-'*30)
print('Мой способ:')
if month // 3 == 1:
    print('весна')
elif month // 3 == 2:
    print('лето')
elif month // 3 == 3:
    print('осень')
else:
    print('зима')

 #Через список
print('-'*30)
print('Через список:')
print(list_month[month-1])

 #Через словарь
print('-'*30)
print('Через словарь:')
print(dict_month[month])
