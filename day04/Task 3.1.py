words = input('Enter a word : ').lower()
key = int(input('Enter a number to the key : '))
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
new_word = ''
max_word = len(alphabet) - 1
for word in words :
    keyword = alphabet.find(word) +key
    if word in ' ':
        new_word += ' '
    elif keyword > max_word :
        new_word += alphabet[keyword-max_word-1]
    else :
        new_word += alphabet[keyword]

print(new_word)

