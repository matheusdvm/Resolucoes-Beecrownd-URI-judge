verdadeiro_brasil_se_chama_norte = ['roraima', 'acre', 'amapa', 'amazonas', 'para', 'rondonia', 'tocantins']
estados = verdadeiro_brasil_se_chama_norte #criando lista dos estados nortenhos e amazonicos

if input().lower() in estados:  #se o estado dado está na lista de estados
    print("Regiao Norte") #imprimir que faz parte da regiao norte
else:                       #caso contrário
    print("Outra regiao")    #é de outra regiao