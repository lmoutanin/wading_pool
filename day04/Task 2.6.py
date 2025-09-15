n =  int(input('Enter a number : '))
x = 2
max = n//x

for i in range(2,max+1):
    table = []
    for j in range (1,max)[::-1]:
        value = i * j
        if  value < n :
            table.append(value)
    print(table)