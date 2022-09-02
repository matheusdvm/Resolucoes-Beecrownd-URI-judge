lista = [0, 0, 0, 0]
for _ in range(5):
    n = int(input())
    if n % 2 == 0:
        lista[0] += 1
    else:
        lista[1] += 1

    if n > 0:
        lista[2] += 1
    elif n < 0:
        lista[3] += 1

print(f"""{lista[0]} valor(es) par(es)
{lista[1]} valor(es) impar(es)
{lista[2]} valor(es) positivo(s)
{lista[3]} valor(es) negativo(s)""")