n = int(input())
numeros =[]
for i in range(1,10001):
    if i%n == 2:
        numeros.append(i)
for i in numeros:
    print(i)