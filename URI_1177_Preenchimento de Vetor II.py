t=int(input())
cont=0
for i in range(1000):
    print('N[{0}] = {1}'.format(i,cont))
    cont+=1
    if cont==t:
        cont=0
