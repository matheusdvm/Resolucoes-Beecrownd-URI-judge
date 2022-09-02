n , s = 0, 0
for _ in range(6):
    i = float(input())
    if i > 0:
        n += 1
        s += i

media = round(s/n,1)

print(f"""{n} valores positivos
{media}""")
