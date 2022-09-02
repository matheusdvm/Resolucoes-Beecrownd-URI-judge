vezes = int(input())
faces_classico =[1,2,3,4,5,6]
while vezes>=1:
    vezes = vezes - 1
    l3 = int(input())
    l1, l2, l6, l5 = (int(x) for x in input().split())
    l4 = int(input())
    faces =[l1,l2,l3,l4,l5,l6]
    if (l1 + l6) != 7 and (l3 + l4) != 7 and (l2 + l5) != 7:
        print("NAO")
    else:
        if sorted(faces) == faces_classico:
            print("SIM")
        else:
            print("NAO")