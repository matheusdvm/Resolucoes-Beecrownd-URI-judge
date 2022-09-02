h,e,a,o,w,x = (int(x) for x in input().split())
triplice_alianca = h + e + a  #quantidade de soldados time do bem
eixo_do_mal = o + w           #quantidade de soldados time do mal

#primeiro, verificar a partir do uso de if, elif e else
#todas as possiveis occorrências
if triplice_alianca<=eixo_do_mal:
    #gandalf chama os reforços
    triplice_alianca = triplice_alianca + x 
    #se numa batalha empatada terminar apenas com o bilbo e o ultimo orc, bilbo vencerá (o lado do bem) 
    if triplice_alianca<eixo_do_mal: 
        print("Sauron has returned.")
    elif triplice_alianca >=eixo_do_mal:
        print("Middle-earth is safe.")
else:
    print("Middle-earth is safe.")