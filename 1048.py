s = float(input())

if 0<=s<=400:
    reajuste = 15
elif 400<s<=800:
    reajuste = 12
elif 800<s<=1200:
    reajuste = 10
elif 1200<s<=2000:
    reajuste = 7
elif s>2000:
    reajuste = 4
else:
    reajuste = 0

s_r = s * (reajuste/100)
novo_salario = s_r + s


print(f"""Novo salario: {novo_salario:.2f}
Reajuste ganho: {s_r:.2f}
Em percentual: {reajuste} %""")