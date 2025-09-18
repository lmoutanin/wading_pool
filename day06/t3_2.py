def func1(char, lenChar):
    return len(char) >= lenChar


def func2(char, lenspecialChar):
    punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                   ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
                   '}', '~', ' ']
    sum = 0
    for i in char:
        if i in punctuation:
            sum += 1
    return sum >= lenspecialChar


def func3(char, lenNumber):
    sum = 0
    for i in char:
        if i.isdigit():
            sum += 1
    return sum >= lenNumber


def passcheck():
    password = input('Enter your paswword : ')
    if type(password) == str:
        if (func1(password, 16)) and (func2(password, 3)) and (func3(password, 1)):
            return True
        else:
            return False
    else:
        print('Error enter a string for password')
        return passcheck()


print(passcheck())
