def max_prefix(s):
    shortest_word = min(s, key=len)
    for i, char in enumerate(shortest_word):
        for word in s:
            if word[i] != char:
                shortest_word = shortest_word[:i]
    return shortest_word

if __name__ == '__main__':
    s = list(input('Введите слова через пробел: ').split(' '))
    print(f'Max prefix is: {max_prefix(s)}')
