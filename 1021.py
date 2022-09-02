n = float(input())

n100 = int(n // 100)
n = n % 100
n50 = int(n // 50)
n = n % 50
n20 = int(n // 20)
n = n % 20
n10 = int(n // 10)
n = n % 10
n5 = int(n // 5)
n = n % 5
n2 = int(n // 2)
n = n % 2

m100 = int(n // 1)
n = n % 1

if 0.0<n<1:
    n = n * 100

m50 = int(n // 50)
n = n % 50
m25 = int(n // 25)
n = n % 25
m10 = int(n // 10)
n = n % 10
m5 = int(n // 5)
n = n % 5
m1 = int(n // 1)
n = n % 1

print(f"""NOTAS:
{n100} nota(s) de R$ 100.00
{n50} nota(s) de R$ 50.00
{n20} nota(s) de R$ 20.00
{n10} nota(s) de R$ 10.00
{n5} nota(s) de R$ 5.00
{n2} nota(s) de R$ 2.00
MOEDAS:
{m100} moeda(s) de R$ 1.00
{m50} moeda(s) de R$ 0.50
{m25} moeda(s) de R$ 0.25
{m10} moeda(s) de R$ 0.10
{m5} moeda(s) de R$ 0.05
{m1} moeda(s) de R$ 0.01""")