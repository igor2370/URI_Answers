lista=input().split()
a=int(lista[0])
for i in lista[1:]:
    i=int(i)
    if i>0:
        n=i
        break

soma=0

for i in range(0,n):
    soma+=a+i
print(soma)
