def sort_simples():
    a , b , c = (int(x) for x in input().split())
    lista= [a,b,c]
    lista.sort()

    for n in lista:
        print(n)
    print()
    for n in (a,b,c):
        print(n)

if __name__ == "__main__":
    sort_simples()