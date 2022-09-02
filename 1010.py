#a resolução é simples, basta multiplicar y numero de peças pelo valor z unitario de cada peça x:
def main():
    total = 0.0   #criando uma variavel float para calcular o total
    for i in range(2):
        x, y, z = input().split()
        y, z = int(y), float(z)
        total += int(y)*float(z)
    print("VALOR A PAGAR: R$ %.2f"%total) 

if __name__ == "__main__":
    main()