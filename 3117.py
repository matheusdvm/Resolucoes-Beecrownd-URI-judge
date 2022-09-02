quantidade_alunos, quantidade_min_pessoas = (int(x) for x in input().split())
lista_horarios = list(input().split())
chegaram_a_tempo=0
if len(lista_horarios) == quantidade_alunos:
    for pessoa in lista_horarios:
        if int(pessoa) <= 0:  #cada pessoa que chegar a tempo soma +1 a unidade
            chegaram_a_tempo += 1  
    
#testando se há pessoas suficientes:
if chegaram_a_tempo >= quantidade_min_pessoas: 
    print("YES")
else:
    print("NO")