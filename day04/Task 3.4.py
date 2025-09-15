def crypt(text, key):
    text = text.lower()
    key = key.lower()
    count_key = 0
    crypt = ''

    for i in text:
        if i == ' ':
            crypt += i
        else:
            f = (alphabet.find(i) + alphabet.find(key[count_key])) % 26
            crypt += alphabet[f]

        if count_key == len(key) - 1:
            count_key = 0
        else:
            count_key += 1
    return crypt, len(key)


FREQUENCY_COUNT = {
    'en': {'a': 8.16, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.22, 'g': 2.01, 'h': 6.09, 'i': 6.96,
           'j': 0.15, 'k': 0.77, 'l': 4.02, 'm': 2.40, 'n': 6.74, 'o': 7.50, 'p': 1.92, 'q': 0.09, 'r': 5.98, 's': 6.32,
           't': 9.05, 'u': 2.75, 'v': 0.97, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07}
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

texts, sizeKey = crypt('hello world', 'max')
texts ='aretssaretss'
lst = []
new_text = texts


texts = texts.split(' ')
texts = ''.join(texts)

print(texts)

count = sizeKey
word = ''

for i in range(len(texts)):
    if i == sizeKey - 1:
        word += texts[i]
        lst.append(word)
        sizeKey += count
        word = ''
    else:
        word += texts[i]

print(lst)
count = 0
letter_count = 0
word_count = 1
frequency = {}

for word in lst:
   for letter in word:
       index = word.find(letter)
       newLst = lst[lst.index(word)+1:]
       for otherWord in newLst :
           if letter == otherWord[index]:
                if index in frequency:
                    if letter in frequency[index]:
                       frequency[index][letter] +=1
                    else:
                        frequency[index] = {letter: 1}
                else:
                    frequency[index] = {letter : 1}


print(frequency)

