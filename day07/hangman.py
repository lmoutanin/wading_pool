import random
from english_words import get_english_words_set

def check_penalities(number):
    return number >= 11


def random_word():
    words = list(get_english_words_set(['web2'], alpha=True, lower=True))
    return random.choice(words)

def word_find(find, word):
    display = ''
    for i in word:
        if i in find:
            display += i
        else:
            display += '_ '
    return display


def input_user(find, word, penalties):
    user = input('$> ').lower().replace(' ', '').upper()
    display = ''
    check = False
    if len(user) == 1:
        if user in word:
            find.append(user)
            for i in word:
                if i in find:
                    check = True
                    display = f'{word}: correct guess - {penalties} penalties'
                else:
                    check = False
                    display = f'Found one {user}'
                    break
        else:
            display = f'No {user} Found'
            penalties += 1
    else:
        if user == word:
            check = True
            display = f'{user}: correct guess - {penalties} penalties'
        else:
            penalties += 5
            display = f'{user}: incorrect guess'
    if check:
        find = word
    print(display)
    return find, penalties


def main():
    word = str(random_word()).upper()
    print(word)
    penalties = 0
    find = []
    while True:
        print(f' {word_find(find, word)} / {penalties} penalties')
        find, penalties = input_user(find, word, penalties)
        if find == word:
            break
        elif check_penalities(penalties):
            print(word)
            print('You loose')
            break
