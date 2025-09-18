
def clean_string():
    x = input('Enter your sentences : ').lower()
    list = []
    punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                   ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
                   '}', '~']
    for i in x :
        list.append(i)

    for i in punctuation :
        if i in list:
            list.remove(i)

    x = ''.join(list)
    if x == x[::-1] :
        print(f'{x} is palindrome')
        return ''
    else:
        print(f"{x} isn't palindrome")
        return clean_string()
clean_string()
