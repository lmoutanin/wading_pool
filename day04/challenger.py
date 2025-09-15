import sys

number = int(input('Enter a number : '))
words = input('Enter a words : ')
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
check = False
new_word = []
if number == 0 :
    sys.exit()

for vowel in vowels:
    if vowel in words :
        print(number)
        check = True
if number >= 42 :
    print(number)
    check = True
if not check :
    print(words)





