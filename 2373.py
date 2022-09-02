n, l, c, total_quebrado= 0 , 0 , 0, 0
n = int(input())
while not n<=0:
    l, c = (int(x) for x in input().split())
    n = n - 1
    if l>c:
        total_quebrado = total_quebrado + c
print(total_quebrado)