n = int(input()) #entrada de quantidade de n peças
l = list((int(x) for x in input().split())) # criar uma lisa de valores a ser testada
t = list(range(1,(n+1)))  #lista teste

for item in l:    
    if item in t:  #remover os itens que não estão em t
        t.remove(item) 

for item in t:  #imprimir as peças faltantes
    print(item)#, end=' ')  #deixar um espaço no final para caso haja
                        # mais uma peça faltando, possa imprimir ao lado
                        # e removi pois apresentou presentantion error no URI