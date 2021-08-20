from math import sqrt
try:
    a, b, c = map(float, input().split(' '))
    
    r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')
    
except:
    print('Impossivel calcular')