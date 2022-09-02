from math import sqrt
def bhaskara():
    a, b, c = (float(x) for x in input().split())
    #calcular o delta
    delta = pow(b,2) -4*a*c
    if delta<0 or a ==0:
        return print("Impossivel calcular")
    #calcular raizes
    r1 = (-(b) + sqrt(delta)) / (2*a)
    r2 = (-(b) - sqrt(delta)) / (2*a)
    
    return print("R1 = %.5f\nR2 = %.5f"%(r1,r2))

if __name__ == "__main__":
    bhaskara()