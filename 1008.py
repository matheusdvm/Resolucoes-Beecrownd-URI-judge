number = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

salario = float(horas_trabalhadas * valor_por_hora)

print("NUMBER = %d" %number)
print("SALARY = U$ %0.2f" %salario)