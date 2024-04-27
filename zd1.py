s = list(input('Введите слова через пробел: ').split(' '))
shortest_word = min(s, key=len)
for i, char in enumerate(shortest_word):
    for word in s:
        if word[i] != char:
            shortest_word = shortest_word[:i]

print(f'Max prefix is: {shortest_word}')