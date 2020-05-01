'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

class Date:
    date_in_str = ""

    def __init__(self, date: str):
        Date.date_in_str = date


    @classmethod
    def extract(cls):
         result = list(map(int, cls.date_in_str.split("-")))
         return {'day': result[0],
                 'month': result[1],
                 'year': result[2]}


    @staticmethod
    def check(date_structure: dict) -> bool:
        if date_structure['month'] <= 0 or date_structure['month'] > 12:
            raise ValueError(f"Не верное значение месяца: {date_structure['month']}")
        else:
            max_day_in_month = 30 if date_structure['month'] in [4, 6, 9, 11] else 31
            if date_structure['month'] == 2:
                max_day_in_month = 28 if date_structure['year'] % 4 or not date_structure['year'] % 100 else 29
            if date_structure['day'] <= 0 or date_structure['day'] > max_day_in_month:
                raise ValueError(f"Не верное значение дня: {date_structure['day']}")
        print("Дата в верном формате")
        return True


new_date = Date("29-02-2000")
date_dict = Date.extract()
print(date_dict)
Date.check(date_dict)
