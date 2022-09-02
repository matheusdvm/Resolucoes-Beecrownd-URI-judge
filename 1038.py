comida=[4.0, 4.5, 5.0, 2.0, 1.5]
a, b = (int(x) for x in input().split())
conta = comida[(a-1)] * b
print("Total: R$ %.2f" % conta)