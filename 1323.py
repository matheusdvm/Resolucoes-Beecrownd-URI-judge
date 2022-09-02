n = 1
while 1<=n<=100:
    lc,qt_quad = [], 0
    n = int(input())
    if n == 0:
        break
    for i in range(1,n+1):
        lc += [i]
    for index in range(0, len(lc)):
        if lc[index] == 1:
            qt_quad += n*n
        elif lc[index] == (len(lc)):
            qt_quad += 1
        else:
            qt_quad += lc[index]*lc[index]
    print(qt_quad)