O=input()
M = []
for i in range(12):
    N = []
    for j in range(12):
        N.append(float(input()))
    M.append(N)
soma = 0
indice_menos=5
indice_mais=7
for i in range(7,12):
    for j in range(indice_menos,indice_mais):
        soma += M[i][j]
    indice_menos-=1
    indice_mais+=1
media = soma/30
if O == 'S':
    print('{:.1f}'.format(soma))
elif O == 'M':
    print('{:.1f}'.format(media))
