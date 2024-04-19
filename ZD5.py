a, b = 0, 1
n = int(input('Введите порядковый номер числа Фибоначчи: '))
for i in range(2, n):
    c = a + b
    a = b
    b = c
print(c)
