testes = int(input())
while testes>=1:
    testes -= 1
    string = str(input())
    nova_str = ''
    
    for char in string:
        if char.islower():
            nova_str += char
    
    print(nova_str[::-1])