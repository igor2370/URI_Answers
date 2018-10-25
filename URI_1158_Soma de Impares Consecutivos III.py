n=int(input())
for j in range(n):
    x,y=input().split()
    x=int(x)
    y=int(y)
    soma=0
    l=[]
    if x%2==0:
        x+=1
        for i in range(y):
            l.append(x)
            x+=2
    else:
        for i in range(y):
            l.append(x)
            x+=2
    for i in l:
        soma+=i
    print(soma)
