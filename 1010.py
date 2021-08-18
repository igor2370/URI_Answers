Cp1, Np1, Vp1 = map(str, input().split())
Cp2, Np2, Vp2 = map(str, input().split())
Cp1, Np1, Vp1, Cp2, Np2, Vp2 = int(Cp1), int(Np1), float(Vp1), int(Cp2), int(Np2), float(Vp2)

total = Np1*Vp1 + Np2*Vp2

print(f'VALOR A PAGAR: R$ {total:.2f}')