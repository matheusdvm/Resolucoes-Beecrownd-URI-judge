vi, resposta = [], '' 
jogadores = ['D', 'E', 'F']
i, n = (int(x) for x in input().split())

for p in range(3): #D, E, F : lista de valores iniciais
    vi += [i]
    
while n>0:
    n -= 1
    a = str(input())
    if a[0] == 'A':
        aluguel, recebedor, pagador, valor = a.split(' ')
        valor = int(valor)
        index1 = jogadores.index(recebedor)
        index2 = jogadores.index(pagador)
        vi[index1] += valor
        vi[index2] -= valor
    elif a[0] == 'C':
        compra, comprador, valor = a.split(' ')
        valor = int(valor)
        index1 = jogadores.index(comprador)
        vi[index1] -= valor
    elif a[0] == 'V':
        venda, vendedor, valor = a.split(' ')
        valor = int(valor)
        index1 = jogadores.index(vendedor)
        vi[index1] += valor

for vf in vi:
    vf = str(vf)
    resposta += vf + ' '

print(resposta[:-1])