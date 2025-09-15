v = [x*x for x in range(1,6)]

def big_number(x):
    numbers = None
    for i in x :
        if numbers is None :
            numbers = i
        elif numbers < i :
            numbers = i
    return numbers

def small_number(x):
    numbers = None
    for i in x :
        if numbers is None :
            numbers = i
        elif numbers > i :
            numbers = i
    return numbers


print(v)
print(small_number(v))
print(big_number(v))
