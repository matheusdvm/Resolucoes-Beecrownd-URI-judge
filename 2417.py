Cv, Ce, Cs, Fv, Fe, Fs = (int(x) for x in input().split())

pontos_c = Cv*3 + Ce
pontos_f = Fv*3 + Fe

if pontos_c > pontos_f:
    print("C")
elif pontos_c < pontos_f:
    print("F")
else:
    if Cs > Fs:
        print("C")
    elif Fs>Cs:
        print("F")
    else:#10 5 18 11 2 18
        print("=")