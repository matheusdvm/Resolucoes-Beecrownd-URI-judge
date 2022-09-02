while True:
    frase = input().lower()
    if frase == '*':
        break
        
    palavras = frase.split()
    letras = ''    

    for palavra in palavras:
        letras += palavra[0]
    
    for l in letras:
        letras = letras.replace(l, '')
        break
    
    if letras == '':
        tautograma = 'Y'
    else:
        tautograma = 'N'
       
    print(tautograma)