alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()


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
    return crypt


def decrypt(text, key):
    text = text.lower()
    key = key.lower()
    count_key = 0
    crypt = ''

    for i in text:
        if i == ' ':
            crypt += i
        else:
            f = (alphabet.find(i) - alphabet.find(key[count_key])) % 26
            crypt += alphabet[f]

        if count_key == len(key) - 1:
            count_key = 0
        else:
            count_key += 1
    return crypt

v = crypt('dcode', 'clecl')
print(v)
print(decrypt(v, 'clecl'))

