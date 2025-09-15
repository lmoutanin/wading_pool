dico = {
    " dalmatians ": 101,
    "pi": 3.14,
    " beast ": 3 * 2 * 111,
    " life ": 42,
    " googol ": 10 ^ 100
}
key = ''
max_values = ''

for i in dico :
    if  max_values == '':
        max_values = dico[i]
        key = i
    elif max_values < dico[i] :
        max_values = dico[i]
        key = i
print(dico)
print(dico[key])