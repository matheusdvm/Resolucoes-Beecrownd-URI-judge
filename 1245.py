while True:
    try:
        testes = int(input())
        pares = 0
        #criar uma lista de valores de sapatos cujo indice será correspondente ao tamanho correspondente
        sapatos = [0 for i in range(61)]  
        
        for times in range(testes):
            tam, lado = (str(x) for x in input().split())
            tam = int(tam)

            if (lado == 'D'):
                if(sapatos[tam] < 0):
                    pares += 1 #formará um par quando adicionarmos 1 a um numero negativo
                sapatos[tam] += 1 #sempre que aparecer um sapato direito adicionar 1
            elif (lado == 'E'):
                if(sapatos[tam] > 0):
                    pares += 1 #formará um par quando subtrairmos 1 a um numero positivo
                sapatos[tam] -= 1 #sempre que ver um esquerdo subtrair 1
            
        print(pares)  # Imprimir a quantidade de pares ao sair do loop for

    except EOFError:  
        break