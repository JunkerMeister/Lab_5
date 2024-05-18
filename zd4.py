def t_or_f(s):
    ans = True
    for i in range(len(s)-1):
        if sorted(s[i]) != sorted(s[i+1]):
            ans = False
        else:
            ans = True
    return ans

if __name__ == '__main__':
    s = list(input('Введите слова через пробел: ').split(' '))
    print(t_or_f(s))