def imprimir_resultado(acertos):
    if acertos == 3:
        print('terno')
    elif acertos == 4:
        print('quadra')
    elif acertos == 5:
        print('quina')
    elif acertos == 6:
        print('sena')
    elif acertos<3:
        print('azar')
        
aposta = list((int(x) for x in input().split()))  #lista de valores da aposta
sorteio = list((int(x) for x in input().split())) #lista de valores premiados
acertos = 0  #numero de acertos totais

for num in aposta:   
    if num in sorteio: # se o numero estiver sorteado
        sorteio.remove(num) #remover o numero para ter certeza que nao ouveram dois identicos no calculos
        acertos += 1 #somar mais um ao total de acertos

#imprimir o resultado a partir da função declarada
imprimir_resultado(acertos)