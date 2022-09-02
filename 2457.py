l = input()
f = input().split(' ')
ctgp = 0

for p in f:
    for let in p:
        if let == l:
            ctgp +=1
            break
p = (ctgp/len(f))*100
print('%.1f' % p)
