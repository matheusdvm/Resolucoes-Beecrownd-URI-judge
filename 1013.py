def eh_maior():
    x, y, z = (int(x) for x in input().split())  #entrada dos valores inteiros
    MaiorXY = int((x + y + abs(x - y)) / 2)  #calcular maior com a formula dada
    a = MaiorXY   #armazenar valor do maior em outra variavel
    MaiorAZ = int((a + z + abs(a - z))/2)  #comparar novamente
    return print(str(MaiorAZ) + " eh o maior")

if __name__ == "__main__":
    eh_maior()