O=input()
M = []
for i in range(12):
    N = []
    for j in range(12):
        N.append(float(input()))
    M.append(N)
soma = 0
indice=11
for i in range(1,11):
    for j in range(indice,12):
        soma += M[i][j]
    if i<5:
        indice -= 1
    elif i==5:
        continue
    elif i>=6:
        indice += 1


media = soma/30
if O == 'S':
    print('{:.1f}'.format(soma))
elif O == 'M':
    print('{:.1f}'.format(media))
