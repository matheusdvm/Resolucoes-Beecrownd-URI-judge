x = []
for i in range(10):
    i = int(input())
    if i<=0:
        x.append(1)
    else:
        x.append(i)
index = 0
for j in x:
    print(f"X[{index}] = {j}")
    index += 1
