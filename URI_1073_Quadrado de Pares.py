n=int(input())
l=[]
for i in range(1,n+1):
    if i%2==0:
        l.append(i)
        l.append(i**2)
for i in range(0,len(l),2):
    print('{0}^2 = {1}'.format(l[i],l[i+1]))
