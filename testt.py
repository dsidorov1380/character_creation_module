from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Невозможно выполнить."""
    if your_number <= 0:
        return
    countable = CalculateSquareRoot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {countable}')


print(message)
calc(25.5)