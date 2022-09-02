L, A, P, R = (int(x) for x in input().split())
R = R + R
D = ((L*L)+(A*A)+(P*P))**(1/2)

if (D <= R):
 print("S")
else:
    print("N")