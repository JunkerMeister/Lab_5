arr = list(map(int, input('Введите последовательность чисел от 1 до N, где одно из чисел удалили. Оставшиеся числа перемешали в случайном порядке.\n Я найду удаленное число: ').split()))
a = sorted(arr)
for i in range(len(a)+1):
    if a[i+1] - a[i] != 1:
        break
    else:
        i += 1
print("Пропущено число:", a[i] + 1)