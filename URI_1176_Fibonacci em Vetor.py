t=int(input())
for j in range(t):
    n=int(input())
    seq=1
    l=[0]
    for i in range(n):
        seq=seq+l[i-1]
        l.append(seq)
    print('Fib({0}) = {1}'.format(n,l[n]))
