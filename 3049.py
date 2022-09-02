#definir função de area do trapezio
def area_trapezio(b, t, h):  #formula disponivel em https://pt.mosg-portal.com/calculate-area-irregular-trapezoid-5960008-1192
    area = ((b+t)/2)*h
    return area

#declarar as variaveis de comprimento e altura da nota
comp_nota = 160  #comprimento
alt_nota = 70    #altura

#dar entrada nos valores de B e T
B = int(input())  # PONTO INICIAL DO CORTE
T = int(input())  # PONTO FINAL DO CORTE
B_linha= comp_nota - B  
T_linha= comp_nota - T

#calcular as areas para realizar análise
area_total = 160*70
felix = area_trapezio(B, T, alt_nota)
marzia = area_trapezio(B_linha, T_linha, alt_nota)

if felix > area_total / 2: #se felix conseguir uma area maior que a metade da total ele consegue    
    print(1)
elif marzia > area_total / 2: #se marzia conseguir uma area maior que a metade da total ele consegue
    print(2)
else:   #qualquer outra possibilidade o valor da nota se perde
    print(0)