while True:
    d, n = (int(x) for x in input().split())
    if d == 0 and n == 0:
        break
    sd = str(d)
    sn = str(n)
    
    for c in sd:
        sn = sn.replace(c, '')
    
    if sn == '':
        sn = '0'
        
    print(int(sn))