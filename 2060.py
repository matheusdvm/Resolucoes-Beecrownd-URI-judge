n = int(input())
numeros = [i for i in (int(x) for x in input().split())]
mult = [2,3,4,5]
r = [0 for i in range(4)]

for numero in numeros:
    index = 0
    for d in mult:
        if numero%d == 0:
            r[index] += 1
        index += 1

index = 0
for i in r:
    print("{} Multiplo(s) de {}".format(i, mult[index]))
    index += 1