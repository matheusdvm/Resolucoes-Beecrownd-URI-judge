testes = int(input())

for t in range(testes):
    str1,str2 = (str(x) for x in input().split())
    nova_str = ''
    if(len(str1) <= len(str2)):
        for char in range(len(str1)):
            nova_str += str1[char]
            nova_str += str2[char]
        nova_str += str2[len(str1):]
    else:
        for char in range(len(str2)):
            nova_str += str1[char]
            nova_str += str2[char]
        nova_str += str1[len(str2):]
    print(nova_str)