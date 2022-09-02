from math import sqrt

for i in range(int(input())):
    numero = int(input())
    eh_primo = True

    if numero % 2 == 0:
        eh_primo = False
        
    elif eh_primo:
        for k in range(3, int(sqrt(numero))+1, 2): 
            if numero % k == 0:
                eh_primo = False
                break

    if eh_primo or numero == 2:
        print("Prime")
    else:
        print("Not Prime")