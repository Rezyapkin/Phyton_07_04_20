
# Задание 4, урок 2

test_str = input('Введите строку: ')

list_words = test_str.split(' ')

num_word = 1
for word in list_words:
    print(f'{num_word}: {word[:10]}')
    num_word += 1
