n = int(input())
results = []
while n>=1:
    x= int(input())
    if x % 2 == 0:
        if x > 0:
            results.append("EVEN POSITIVE")
        elif x < 0:
            results.append("EVEN NEGATIVE")
        else:
            results.append("NULL")
    elif x % 2 != 0:
        if x>0:
            results.append("ODD POSITIVE")
        elif x<0:
            results.append("ODD NEGATIVE")
    n = n - 1
for i in results:
    print(i)
