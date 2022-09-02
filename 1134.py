a, g, d = [], [], []
x=0
while x!=4:
    y = int(input())
    if y==1:
        a.append(1)
    elif y==2:
        g.append(1)
    elif y==3:
        d.append(1)
    elif y==4:
        x=4

print("MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d"%(sum(a), sum(g), sum(d)))
