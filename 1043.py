a, b, c = (float(x) for x in input().split())

dif_a = b-c
if dif_a<0:
    dif_a = dif_a*(-1)
dif_b = a-c
if dif_b<0:
    dif_b = dif_b*(-1)
dif_c = a-b
if dif_c<0:
    dif_c = dif_c*(-1)

if a>dif_a and b>dif_b and c>dif_c:
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)
else:
    area = (a+b)*c*(1/2)
    print("Area = %.1f" % area)