# dona monica possui a idade correspondente à soma dos 3 filhos
m, a, b = 0, 111, 111
while not (40<=m<=110):  #adicionando restrições
    m = int(input())

while (1<=a,b<m) and not a!=b: #adicionando restrições
    b = int(input())
    a = int(input())

c = m - a - b     # descobrir a idade do terceiro filho

filhos = [a, b, c]  #adicioná-los na lista
print(max(filhos))  #imprimir a idade do mais velho a partir da funçao max