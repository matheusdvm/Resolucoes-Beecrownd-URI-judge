n = int(input())
resultado=[]
while n>=1:
    soma =[]
    x, y = (int(x) for x in input().split())
    if x>y:
        for i in range(y+1, x):
            if i%2 != 0:
                soma.append(i)
    elif y>x:
        for i in range(x+1, y):
            if i%2 != 0:
                soma.append(i)
    else:
        soma.append(0)
    s = sum(soma)
    resultado.append(s)
    n = n-1
for i in resultado:
    print(i)
    
