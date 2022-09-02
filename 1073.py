from math import pow
n = int(input())
numeros =[]

if 5 < n < 2000:
    for i in range(1,(n+1)):
        if i % 2 == 0:
            numeros.append(i)

for i in numeros:
    print("%d^2 = %d" % (i, pow(i,2)))