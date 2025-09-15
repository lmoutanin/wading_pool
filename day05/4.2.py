lst = [1, 1, 2, 2, 3]
other_lst = ['a', 2, 'a', 2, 'A']

def remove_duplicate_element(x):
    new_lst = []
    for i in x :
        if i not in new_lst :
            new_lst.append(i)
    return new_lst

print(remove_duplicate_element(lst))
print(remove_duplicate_element(other_lst))


