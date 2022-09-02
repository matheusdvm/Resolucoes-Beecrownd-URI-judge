p1,p2,n,m = 2, -1, 0, -2
while not p1<=n and not p2<=m:
    lista1, lista2 = [], []    
    n, m = (int(x) for x in input().split())
#Para achar o maior primo utilizei osconhecimentos
 #  de exercicios feitos sobre o Crivo de Eratóstenes 
  # para encontrar um numero primo
    #achar lista_primos do juilherme
    for numero in range(1,n+1):
        lista1.append(numero)
        x = 0
        for k in range(1,n+1):
            if numero%(k+1) == 0: 
                x = x + 1
                if x == 2:
                    lista1.remove(numero)
        
    #achar lista_primos do jojerio
    for numero in range(1,m+1):
        lista2.append(numero)
        x = 0
        for k in range(1,m+1):
            if numero%(k+1) == 0: 
                x = x + 1
                if x == 2:
                    lista2.remove(numero)
    p1, p2 = max(lista1), max(lista2)

print(p1*p2)