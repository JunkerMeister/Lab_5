s = list(input('Введите слова через пробел: ').split(' '))
ans = True
for i in range(len(s)-1):
    if sorted(s[i]) != sorted(s[i+1]):
        ans = False
    else:
        ans = True
print(ans)
