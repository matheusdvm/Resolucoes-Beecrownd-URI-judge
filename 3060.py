v, p, resto= 0, 0, 0 
resultado = []  #lista das parcelas

while not (10<=v<=1000):
    v = int(input()) #representa o valor da compra
while not (2<=p<=18):
    p = int(input()) #representa a quantia das parcela

if v%p == 0:   #verifica se o valor é divisivel por p
    parcela = int(v/p)  #se sim, a parcela terá o valor apresentado
elif v%p !=0:  #verifica se o valor não é divisivel por p
    resto = v%p #se sim, calcula-se o resto, e distribui nas demais parcelas
    parcela = int((v - resto)/p)
    
for i in range(0, p):                   #adicionar ao resultado as parcelas com valor calculado sem o resto
    resultado.append(parcela)
    
if resto !=0:                           #debbug #1
    for i in range(0,(resto)):              #distribuir uma unidade às primeiras parcelas para cada "resto"
        resultado[i] = parcela + 1
    
for i in resultado:                  #dar o output do resultado
    print(i)