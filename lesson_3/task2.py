
# Задание 2, урок 3

def print_info(first_name: str, last_name: str, **info):
    # Выводит на экран информацию о человеке, контактная информация передается через именованные параметры **info
    str_info = ''
    for key, value in info.items():
        str_info += f'{"; " if str_info else ""}{key}: {value}'
    print(f'{first_name} {last_name} ({str_info})')


print_info('Dmitry','Rezyapkin',phone='+7977777777',email='a@a.ru')
print_info('Mike','Ivaon',birhday='12.01.2000',email='b@b.ru')
