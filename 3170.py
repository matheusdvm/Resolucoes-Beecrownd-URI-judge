from math import floor

bolinhas = int(input())
galhos = int(input())

#primeiro calcular o numero de bolinhas necessárias:

if galhos%2 != 0:                           #se for impar esse valor será arrendondado para baixo
    bolinhas_nec = int(floor(galhos/2))     #a função floor garante o arrendondamento para baixo
else:
    bolinhas_nec = int(galhos/2)

#segundo verificar se possui todas falta ou não de bolinhas

if bolinhas_nec > bolinhas:
    bolinhas_que_faltam = int(bolinhas_nec - bolinhas)  
    print(f"Faltam {bolinhas_que_faltam} bolinha(s)")
elif bolinhas_nec <= bolinhas:
    print("Amelia tem todas bolinhas!")