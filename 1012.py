A, B, C = map(float, input().split(' '))

triangulo = A*C/2
circulo = 3.14159*C**2
trapezio = (A+B)*C/2
quadrado = B**2
retangulo = A*B

print(f'TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}')