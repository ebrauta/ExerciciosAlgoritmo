HT = int(input("Horas Trabalhadas: "))
VH = float(input("Valor Hora Trabalhada: "))
PD = float(input("Percentual de Desconto: "))
SB = HT * VH
TD = (PD / 100) * SB
SL = SB - TD
print(SB)
print(SL)