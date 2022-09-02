def imprimir(respostas):
    if len(respostas) > 1:
        print('*')
    elif len(respostas) == 1:
        print(respostas[0])
    else:
        print('*')
            

while True:
    n = int(input())
    if n == 0:
        break
    else:
        for j in range(n):
            a,b,c,d,e = (int(x) for x in input().split())
            dicio = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e}
            respostas = []
            for m,v in dicio.items():
                if v <= 127:
                    respostas.append(m)
            imprimir(respostas)