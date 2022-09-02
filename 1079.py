n = int(input())
while n>0:
    x,y,z = (float(x) for x in input().split())
    media = (2*x + 3*y + 5*z)/10
    print(round(media,1))
    n -= 1