n = int(input())
coelhos, ratos, sapos = 0,0,0

while n>0:
    q,t = input().split()
    q = int(q)
    
    if t == 'C':
        coelhos += q
    elif t == 'R':
        ratos += q
    elif t == 'S':
        sapos += q
        
    n-=1

total = coelhos + ratos + sapos

pc = (coelhos/total)*100
pr = (ratos/total)*100
ps = (sapos/total)*100

print(f"""Total: {total} cobaias
Total de coelhos: {coelhos}
Total de ratos: {ratos}
Total de sapos: {sapos}
Percentual de coelhos: {pc:.2f} %
Percentual de ratos: {pr:.2f} %
Percentual de sapos: {ps:.2f} %""")
