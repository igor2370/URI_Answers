x=[]
for i in range(20):
    x.append(int(input()))
for i in range(10):
    x[i],x[19-i]=x[19-i],x[i]
for i in range(20):
    print('N[{0}] = {1}'.format(i,x[i]))
