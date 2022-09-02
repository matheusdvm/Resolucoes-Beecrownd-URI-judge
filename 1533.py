n = int(input())
while n != 0:
    l1 = list((int(x) for x in input().split()))
    l2 = l1.copy()
    remover_maior = l1.pop((l1.index(max(l1))))
    segundo_maior = max(l1)
    print(l2.index(max(l1))+1)
    n = int(input())  
