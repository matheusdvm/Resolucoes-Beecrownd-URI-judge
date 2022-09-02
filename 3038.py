while True:  #laço while infinito que termina em EOF
    try:
        txt = str(input())   #inserir uma str
#print("a maneira abaixo ocorre time speed limit pois existe a maneira de substituir \n a função .replace por outra (.maketrans) que se utiliza de uma conjunto de tradução, no caso: \n o conjunto de @&!*# de uma str será substituida pelos elementos respectivos'aeiou'")
#         crypto ={'@':'a','&':'e','!':'i','*':'o','#': 'u'} #gerar um dicionario dos valores cryptografados no texto
#         for key in crypto:
#             valor = crypto[key]
#             if key in txt:  #se o caractere está no txt
#                 txt = txt.replace(key, valor) #substituir o caractere pelo valor correspondente do dicionario
#          print(txt,end='\n')  #imprimir texto com quebra de linha
    
#para solucionar o troblema basta seguir os seguintes passos:
#primeiro:
  #fazer o conjunto de tradução c'
        c= str.maketrans('@&!*#','aeiou')
#segundo:
  #traduzir a variavel str (txt) a partir da tabela criada (c)
        print(txt.translate(c))   #a função translate realiza a tradução dos termos "@&!*#" pelo indice de "aeiou' (0,1,2,3,4)
        
    except EOFError:
        break