n, v = [], int(input())

for i in range(10):
    n.append(v)
    v *= 2

index = 0
for j in n:
    print(f"N[{index}] = {j}")
    index += 1