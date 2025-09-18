import time



def cal_power(number,power):
    return number ** power

temps_passé = time.time()

print(cal_power(42,84))
temps_passé = time.time()


print(cal_power(42,168))
print(time.time() - temps_passé)

