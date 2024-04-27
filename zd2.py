from random import randint
arr = ([randint(0, 1001) for x in range(10)])
s_arr = sorted(arr)
n = randint(0, 9)
Delarr = (arr[0:n]+arr[n+1:])
ans = sum(arr) - sum(Delarr)
print(f'Начальный массив: {s_arr} \n Полученный массив: {Delarr} \n Удаленное число: {ans}')