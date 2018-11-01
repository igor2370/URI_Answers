O=input()
M = []
for i in range(12):
    N = []
    for j in range(12):
        N.append(float(input()))
    M.append(N)
soma = 0
indice_menor=1
indice_maior=11
for i in range(0,5):
    for j in range(indice_menor,indice_maior):
        soma += M[i][j]
    indice_menor+=1
    indice_maior-=1
media = soma/30
if O == 'S':
    print('{:.1f}'.format(soma))
elif O == 'M':
    print('{:.1f}'.format(media))
