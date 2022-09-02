N = int(input())
A, L, P = (int(x) for x in input().split())

dif_A = A - N
dif_L = L - N
dif_P = P - N

if dif_A >=0:
    if dif_L >=0:
        if dif_P >=0:
            print("S")
        else:
            print("N")
    else:
        print("N")
else:
    print("N")