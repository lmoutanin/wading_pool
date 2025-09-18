def func1(char,lenChar):
    return len(char) >= lenChar

def func2(char,lenspecialChar):
    punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                   ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
                   '}', '~',' ']
    sum = 0
    for i in char:
        if i in punctuation:
            sum += 1
    return sum >= lenspecialChar


def func3(char,lenNumber):
    sum = 0
    for i in char:
        if i.isdigit() :
            sum +=1
    return sum >= lenNumber

def passcheck(password):
    if  func1(password,16) == True:
        if func2(password,3) == True:
            if func2(password,1) == True:
                return True
    return False




print(func1('lol',3))
print(func2('lol@:#;',3))
print(func3('sbhsbhjkds3323',2))

