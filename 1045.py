def tipos_triangulos():
    while True:
        a,b,c = (float(x) for x in input().split())
        if a>0 and b>0 and c>0:
            break
            
    l =[a,b,c]  #lados do triangulo em lista
    l.sort(reverse = True)  #deixar em ordem decrescente
    
    #definir valores de referencia
    A, B, C = l[0], l[1], l[2]
    
    if A>=(B+C):
        print("NAO FORMA TRIANGULO")
    elif pow(A,2) == (pow(B,2) + pow(C,2)):
        print("TRIANGULO RETANGULO")
    elif pow(A,2) > (pow(B,2) + pow(C,2)):
        print("TRIANGULO OBTUSANGULO")
    elif pow(A,2) < (pow(B,2) + pow(C,2)):
        print("TRIANGULO ACUTANGULO")
    
    
    if A==B==C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B==C or A==C:
        print("TRIANGULO ISOSCELES")

if __name__ == "__main__":
    tipos_triangulos()
        