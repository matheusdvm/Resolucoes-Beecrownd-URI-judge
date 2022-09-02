q = int(input())
l = list(int(x) for x in input().split())

q = q/2

if sum(l)>=q:
    print('N')
else:
    print('Y')