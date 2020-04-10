
# Задание 5

revenue = input('Введите выручку предприятия\n')
expenses = input('Введите расходы предприятия\n')

#Преобразую к числу, проверку "на дурака" не делаю. В задании не было об этом. Поэтому просто преобразую

revenue = float(revenue)
expenses = float(expenses)

profit = revenue - expenses

if profit > 0:
    print(f'Фирма сработала в прибыль {profit:.2f}')
    profitability = profit / revenue * 100
    print(f'Рентабельность составила {profitability:.2f} %\n')
    count_personal = input('Введите количество сотрудников предприятия')
    count_personal = int(count_personal)
    if count_personal > 0:
        print(f'Прибыль на одного сотрудника составила: {profit/count_personal:.2f}')
    else:
        print('Видимо сотрудников заменили роботы)')
elif profit == 0:
    print(f'Фирма сработала в 0')
else:
    print(f'Фирма сработала в убыток {-profit:.2f}')

