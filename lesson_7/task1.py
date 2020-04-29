'''

Задание 1. Урок 7. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

'''


class Matrix:
    def __init__(self, list_of_list):
        # Список списков может передать не матрицу, размерность вложенных список может отличаться. Добьем нулями.
        max_len_row = max(map(len, list_of_list))
        # Вопрос преподователю! Можно ли нулями было еще проще добить чем в строчке ниже?
        self.matrix = [row + [0 for _ in range(max_len_row - len(row))] for row in list_of_list]

    def __str__(self):
        # Для красивого вывода найдем количество символов необходымых для вывода каждого элемента матрицы
        list_len_str = [map(lambda x: len(str(x)), row) for row in self.matrix]
        max_len = max([max(row) for row in list_len_str])
        # Добьем элементы пробелами, чтобы выровнять колонки
        matrix_str = [list(map(lambda x: str(x) + " " * (max_len - len(str(x))), row)) for row in self.matrix]
        return '\n'.join(["    ".join(row) for row in matrix_str])


    @property
    def shape(self):
        return len(self.matrix), len(self.matrix[0])


    def __add__(self, other):
        if self.shape == other.shape:
            res_list = [list(map(lambda x, y: x + y, self.matrix[i], other.matrix[i])) for i in range(self.shape[0])]
            return Matrix(res_list)
        else:
            print(f'Размерность матриц не совпадает: {self.shape} и {other.shape}. Выполнение операции не возможно!')
            raise ValueError


my_matrix1 = Matrix([[2, 4, 6, 6, 3],
                     [3, 34, 333, 3, 3]])

my_matrix2 = Matrix([[6, 2, 3, 4, 6],
                     [4, 123, 85, 2, 1]])

print(my_matrix1)
print("+" * 30)
print(my_matrix2)
print("=" * 30)
print(my_matrix1 + my_matrix2)
