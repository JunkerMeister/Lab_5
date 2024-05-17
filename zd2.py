from random import randint
def rand_list(a, f):
    arr = a
    Delarr = f
    return sum(arr) - sum(Delarr)

if __name__ == '__main__':
    a = ([randint(0, 1001) for x in range(10)])
    b = sorted(a)
    n = randint(0, 9)
    f = (a[0:n] + a[n + 1:])
    c = rand_list(a, f)
    print(f'Начальный массив: {b} \n Полученный массив: {f} \n Удаленное число: {c}')