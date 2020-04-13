
# Задание 1

some_string = 'Привет мир'
some_int = 123456789
some_float = 1.23456789
some_boolean = True
some_list = [1, 2, 3, 4]
some_tuple = (1, 2, 3, 4)

print(some_string)
print(some_int)
print(some_boolean)
print(some_list)
print(some_tuple)

name = input('Как вас зовут?\n')
years_old = input('Сколько Вам лет?\n')
moms_name = input('Как зовут Вашу маму?\n')
moms_years_old = input('Сколко вашей маме лет?\n')

if years_old.isdigit() and moms_years_old.isdigit():
    #Возрасты введены верно. Делаем расчет
    moms_years_old = int(moms_years_old)
    years_old = int(years_old)

    diff_years = abs(moms_years_old - years_old)
    diff_years_str = str(diff_years)

    diff_years_mod100 = diff_years % 100
    diff_years_mod10 = diff_years % 10

    if diff_years_mod100 >= 10 and diff_years_mod100 <= 20:
        diff_years_str += ' лет'
    elif diff_years_mod10 == 1:
        diff_years_str += ' год'
    elif diff_years_mod10 in range(2,5):
        diff_years_str += ' года'
    else:
        diff_years_str += ' лет'
    print(f'{moms_name} страше Вас на {diff_years_str}' if moms_years_old > years_old else 'Ваша мама моложе Вас!)')
else:
    #Если возрасты введены не верно
    print(f'{name} Вы ввели не возраст не верно')

