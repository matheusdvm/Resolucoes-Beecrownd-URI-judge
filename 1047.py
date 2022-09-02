def main():
    hi,mi,hf,mf = (int(x) for x in input().split())
    
    i = hi * 60 + mi
    f = hf * 60 + mf
    x, h, m = 0, 0, 0
    
    if(f > i):
        x = f - i
        h = x / 60
        m = x % 60
        h, m = int(h), int(m)
        print("O JOGO DUROU", h, "HORA(S) E", m, "MINUTO(S)")
    else:
        f = f + 24 * 60
        x = f - i
        h = x / 60
        m = x % 60
        h, m = int(h), int(m)
        print("O JOGO DUROU", h, "HORA(S) E", m, "MINUTO(S)")
    
if __name__ == "__main__":
    main()
