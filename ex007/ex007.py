A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
if(A < B + C) and (B < A + C) and (C < A + B):
    if(A == B) and (B == C):
        print("Triângulo Equilátero")
    else:
        if(A == B) or (A == C) or (B == C):
            print("Triângulo Isóceles")
        else:
            print("Triângulo Escaleno")
else:
    print("As medidas não formam um triângulo")

