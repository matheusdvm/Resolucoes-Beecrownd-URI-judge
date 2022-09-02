dia = int(input())
resto_dia_ano = dia%365
ano = (dia - resto_dia_ano)/365  #ANO
dias = resto_dia_ano%30  #DIAS
mes = (resto_dia_ano - dias)/30 #MES

print("%.0f ano(s)\n%.0f mes(es)\n%.0f dia(s)" %(ano, mes, dias))
