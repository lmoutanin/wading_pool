x = int(input('Enter a number : '))
message = ''
match x:
    case 42:
        message = 'a'
    case _ if x <= 21:
        message = 'b'
    case _ if x % 2 == 0:
        message = 'c'
    case _ if x / 2 < 21:
        message = 'd'
    case _ if (x % 2 != 0) and (x >= 45):
        message = 'e'
    case _:
        message = 'f'
print(message)
