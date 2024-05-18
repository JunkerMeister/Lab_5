import math

def fibonaci(n):
    c = int((((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5))
    return c


if __name__ == '__main__':
    n = int(input('Введите порядковый номер числа Фибоначчи: '))
    print(f'Ваше число: {fibonaci(n)}')
