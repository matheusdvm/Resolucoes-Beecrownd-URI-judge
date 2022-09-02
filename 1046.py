def main():
    i,f = (int(x) for x in input().split())
    a = 24 - i + f
    while a > 24:
        a -= 24
    print("O JOGO DUROU",a,"HORA(S)")

if __name__ == "__main__":
    main()
    