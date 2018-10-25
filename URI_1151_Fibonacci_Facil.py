n=int(input())
seq=1
l=[0]
for i in range(n-1):
    seq=seq+l[i-1]
    l.append(seq)
for i in l:
    if i==l[-1]:
        print(i)
    else:
        print(i,end=' ')
