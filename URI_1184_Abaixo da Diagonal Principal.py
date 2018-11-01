T=input()
M = []
for i in range(12):
    N = []
    for j in range(12):
        N.append(float(input()))
    M.append(N)
soma = 0
indice=1
for i in range(1,12):
    for j in range(indice):
        soma += M[i][j]
    indice+=1
    if indice==12:
        break
media = soma/66
if T =='S':
    print('{:.1f}'.format(soma))
elif T=='M':
    print('{:.1f}'.format(media))
