carrinhos, bonecas = 0,0   #variaveis de quantidade dos tipos de brinquedos
for i in range(int(input())):    #input indica quantidade de cartas 
    nome, sexo = input().split()  #separa o nome e o sexo de cada carta
    if sexo == 'F':   #se F ganha boneca
        bonecas += 1
    elif sexo == 'M':  #se M ganha carrinho
        carrinhos += 1
print('{} carrinhos'.format(carrinhos))  #imprimir quantidade carrinhos
print('{} bonecas'.format(bonecas))  #imprimir quantidade bonecas
