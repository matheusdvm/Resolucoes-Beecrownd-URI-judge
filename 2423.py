n_bolos = 0  # quantidade de bolos iniciais

#declarar tres valores inteiros
#a - xicaras de farinha 2 por bolo
#b - unidades de ovos  3 por bolo
#c - colheres de leite 5 por bolo
a, b, c = (int(x) for x in input().split())  

while a>=2 and b>=3 and c>=5: #utilizando while é possivel ir diminuindo os valores
    a = a - 2   #enquanto while é verdadeiro,
    b = b - 3   #diminui-se as variaveis pelos valores necessários por bolo
    c = c - 5   #em cada um das variaveis a, b, c (farinha, ovos e leite)
    n_bolos = n_bolos + 1 #soma-se um bolo à quantidade total

print(n_bolos)    #dar o output do resultado