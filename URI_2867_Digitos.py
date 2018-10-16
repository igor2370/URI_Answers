c=int(input())
for i in range(c):
    n,m=input().split()
    n=int(n)
    m=int(m)
    x=n**m
    x=len(str(x))
    print(x)
