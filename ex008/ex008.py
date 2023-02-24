'''
    O operador de disjunção exclusiva (XOR) não existe no Python
    porém pode-se substituuir pelas expressões:
        (R2 == 0) and (R3 != 0)) or ((R2 != 0) and (R3 == 0))
    ou
        (R2 == 0 or R3 == 0) and (R2 != R3)
'''
N = int(input("N: "))
R2 = N - 2 * N//2
R3 = N - 3 * N//3
if ((R2 == 0) and (R3 != 0)) or ((R2 != 0) and (R3 == 0)): 
    print(N)