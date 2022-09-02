x, y, soma = int(input()), int(input()), 0

def somar(menor, maior):
    global soma
    for i in range(menor+1, maior):
        if i % 2 != 0:
            soma += i
    return print(soma)

if x > y:
    somar(y, x)
elif y > x:
    somar(x, y)
else:
    print(soma)
