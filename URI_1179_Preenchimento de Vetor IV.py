cont=0
par=[]
impar=[]
for i in range(15):
    n = int(input())
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    if len(par)==5:
        for j in range(5):
            print('par[{0}] = {1}'.format(j,par[j]))
        par=[]
    elif len(impar)==5:
        for j in range(5):
            print('impar[{0}] = {1}'.format(j,impar[j]))
        impar=[]
if len(impar)>0:
    for i in range(len(impar)):
        print('impar[{0}] = {1}'.format(i, impar[i]))
if len(par)>0:
    for i in range(len(par)):
        print('par[{0}] = {1}'.format(i, par[i]))
