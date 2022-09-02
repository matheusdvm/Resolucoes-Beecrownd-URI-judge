p1 = list((int(x) for x in input().split()))
p2 = list((int(x) for x in input().split()))
compativel = False
index = 0


for p in p1:
    soma = p + p2[index]
    if soma == 2:
        compativel = False
        print('N')
        break
    elif soma == 1:
        compativel = True
    else:
        compativel = False
        print("N")
        break
    index += 1

if compativel == True:
    print('Y')