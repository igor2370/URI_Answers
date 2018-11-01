from math import trunc

t=int(input())
for i in range(t):
    pa,pb,g1,g2=input().split()
    pa=int(pa)
    pb=int(pb)
    g1=float(g1)/100
    g2=float(g2)/100
    anos=0
    while pa<=pb:
        pa+=trunc(pa*g1)
        pb+=trunc(pb*g2)
        anos+=1
        if anos>100:
            break
    if anos<=100:
        print('{} anos.'.format(anos))
    else:
        print('Mais de 1 seculo.')
