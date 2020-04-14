
# Задание 6, урок 3

def int_func(text: str) -> str:
    '''
    Такая функция уже есть в Python - capitalize(). Не проблема напишем)))
    :param text:
    :return:
    '''
    return text[0].upper()+text[1:] if text else ''


some_str = input('Введите строку\n')

list_words = some_str.split(' ')
new_list = list(map(int_func,list_words))
new_str = ' '.join(new_list)
print(new_str)

#Аналогичное можно было сделать проще
print(some_str.title())