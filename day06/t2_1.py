


def puissance(n):
    if n == 0 :
        return 0
    else:
       return n + puissance(n-1)


sum = puissance(42)
print(sum)