def beecrowd_1041():
    x, y = (float(a) for a in input().split())
    
    if x == 0 and y != 0:
        print("Eixo Y")
    elif x != 0 and y == 0:
        print("Eixo X")
    elif x > 0:
        if y > 0:
            print("Q1")
        elif y < 0:
            print("Q4")
    elif x < 0:
        if y > 0:
            print("Q2")
        elif y < 0:
            print("Q3")
    else:
        print("Origem")
        

if __name__ == "__main__":
    beecrowd_1041()
