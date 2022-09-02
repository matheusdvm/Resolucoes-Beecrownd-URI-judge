n=int(input())
while n!=0:
    r = list((int(x) for x in input().split()))
    tamanho = len(r)
    joao = sum(r)
    maria = tamanho - joao
    print('Mary won {} times and John won {} times'.format(maria, joao))
    n=int(input())