x,y=input().split()
x=int(x)
y=int(y)
cont=x

for i in range(1,y+1):
    if i==x:
        print(i,end='')
        print()
        x += cont
    else:
        print(i, end=' ')
