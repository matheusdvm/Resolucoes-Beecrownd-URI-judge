n, gastos, verbas = 0, [], []   #criar lista dos gastos e verbas

while not (n>=1 and n<=100000):  #adicionando o numero de valores citados
    n = int(input())
    
while n>=1:
    n = n - 1
    t, c = (str(x) for x in input().split())   #declarar valores
    c = int(c)
    if t == "G":    #adicionando os valores às listas correspondentes
        gastos.append(c)
    elif t == "V":
        verbas.append(c)
#calcular o valor total de gastos necessarios e verbas disponiveis
total_gastos = sum(gastos)
total_verbas = sum(verbas)

#comparar quem é maior e dar o print
if total_verbas>=total_gastos:
    print("A greve vai parar.")
elif total_gastos>total_verbas:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
