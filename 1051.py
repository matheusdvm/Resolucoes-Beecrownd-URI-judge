r = float(input())
while True:
    if r<=2000:
        imposto = 0
        break
    elif 2000<r<=3000:
        imposto = (r-2000)*0.08
        break
    elif 3000<r<=4500:
        imposto = 80 + (r-3000)*0.18
        break    
    elif r > 4500:
        imposto = 80 + 1500*0.18 + (r-4500)*0.28
        break
    else:
        imposto = 0
        break

if imposto == 0:
    print("Isento")
else:
    print(f"R$ {imposto:.2f}")