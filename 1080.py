x = 100
lista = []
while x>=1:
    x = x - 1
    lista.append(int(input()))
y = max(lista)
z = lista.index(y) + 1
print(y)
print(z)