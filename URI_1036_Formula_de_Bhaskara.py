from math import sqrt
A,B,C=input().split()
A=float(A)
B=float(B)
C=float(C)
if A==0:
    print('Impossivel calcular')
else:
    DELTA = (B**2)-4*A*C
    if DELTA<0:
        print('Impossivel calcular')
    else:
        R1 = (-B+sqrt(DELTA))/(2*A)
        R2 = (-B-sqrt(DELTA))/(2*A)
        print('R1 = {:.5f}'.format(R1))
        print('R2 = {:.5f}'.format(R2))
