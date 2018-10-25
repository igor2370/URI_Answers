s=0
a=b=1
while a<39:
    s+=a/b
    a+=2
    b=b*2
print('{:.2f}'.format(s))
