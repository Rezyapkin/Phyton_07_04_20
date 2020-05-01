'''
Задание 3. Урок 8.
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
'''

class MyClassException(Exception):
    def __init__(self, txt):
        self.txt = txt


list_num = []

while True:
    new_input = input('Введите новый элемент списка (если хотите завершить ввод, введите "stop") ')
    if new_input.lower() == "stop":
        break
    #Решил проверку на число не делать через try - except ValueError, т.к. нужен свой обработчик ошибок
    try:
        if not new_input.replace('.', '', 1).isdigit():
            raise MyClassException('Вы ввели не число')
        list_num.append(float(new_input))
    except MyClassException:
        print('Вы ввели не число')

print(list_num)
