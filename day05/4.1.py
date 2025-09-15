lst_ambassador = ['jojo','lea','koko','zoe','zara']

name = ['damien','cyril','mathieu','gaby','big-jo']

name.extend(lst_ambassador)
name.sort(reverse=True)


for i in name :
    if i in lst_ambassador :
        print(f'Welcome in {i}')
    else :
        print(f'Get lost {i}')
