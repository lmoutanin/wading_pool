
def small_number(x) :
    numbers = None
    for i in x :
        if numbers is None :
            numbers = i
        elif numbers > i :
            numbers = i
    return numbers

def descending_sort(x):
    lst = []
    while len(x) != 0 :
        number = small_number(x)
        lst.append(number)
        x.remove(number)
    return lst

li = [3,12,45,21,2,4,3]

print(descending_sort(li))