n,i,f= (int(x) for x in input().split()) #variaveis utilizadas no exercicio
vetor = list((int(x) for x in input().split()))  #variavel do vetor
contagem = 0  #variavel para a contagem de pares que satisfazem

# um laço FOR que represente cada valor na lista
for valor1 in range(n):
    for valor2 in range(valor1,n):#e um outro laço FOR para comparar esse valor do primeiro laço FOR
        soma = vetor[valor1] + vetor[valor2]                     # com os valores da lista VETOR.
        if valor1 != valor2 and soma >= i and soma<=f:   #verifica se satisfaz
            contagem += 1  #se sim, soma-se a contagem em +1
print(contagem)