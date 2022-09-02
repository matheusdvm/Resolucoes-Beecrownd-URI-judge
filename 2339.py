c, p, f = (int(x) for x in input().split())
papeis_necessarios = c * f
if p>=papeis_necessarios:
    print("S")
else:
    print("N")