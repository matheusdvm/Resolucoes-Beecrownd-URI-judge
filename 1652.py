x, y = (int(x) for x in input().split())
irgl_sing, irgl_plural, casos, resposta = [], [], [], []

while x>0:
    x -= 1
    irgl_1, irgl_2 = (str(x) for x in input().split())
    irgl_sing.append(irgl_1)
    irgl_plural.append(irgl_2)

while y>0:
    y -= 1
    palavra = str(input())
    casos.append(palavra)
    
for p in casos:
    if p in irgl_sing:
        resposta.append(irgl_plural[irgl_sing.index(p)])
    else:
        if (p[-1] == 'y') and (p[-2] not in ('a','e','i','o','u')):
            new = p[:-1] + 'ies'
        elif p[-1] in ('o', 's', 'x'):
            new = p + 'es'
        elif p[-2:] in ('ch','sh'):
            new = p + 'es'
        else:
            new = p + 's'
        resposta.append(new)

for r in resposta:
    print(r)
