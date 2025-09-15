import random
import time

start = time.time()
lst = [x-random.randint(0,10) for x in range(0,1000000)]
lst.sort()
print(lst)
print(time.time()- start)