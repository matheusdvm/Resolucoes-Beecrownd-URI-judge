a, b, c = input().split()
a= int(a)
b= int(b)
c= int(c)

x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

# Primeiro determinar quantos conteners cabem A com X
resto_a = x%a
primeiro = (x - resto_a)/a
# Segundo determinar quantos contener cabem B com Y
resto_b = y%b
segundo = (y - resto_b)/b
# Terceiro determinar quantos contener cabem C com Z
resto_c = z%c
terceiro = (z - resto_c)/c
# Multiplicar primeiro, segundo e terceiro dando o total de conteners
total = primeiro * segundo * terceiro
# Print Resultado
print(int(total))