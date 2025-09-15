# Task 4.1

#
# def test1(x):
#     sum = 0
#     x = int(x)
#     x= str(x)
#     for i in range(len(str(x))):
#         sum += int(x[i])
#     return sum
#
# table1 =  [123434565.2,345567426,44490320097,12.24,424242.8412]
#
# for i in range(len(table1)):
#     print(test1(table1[i]))

n = 201
sumx =  6 + n ** 2
for i in reversed(range(3,n,2)):
    sumx = 6 + ((i ** 2)/sumx)


print((1**2)/sumx)




