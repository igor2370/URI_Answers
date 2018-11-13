from math import sqrt, trunc
while 1:
    n = list(map(int,input().split()))
    if n[0] == 0:
        break
    else:
        a, b, c = n
        lado = trunc(sqrt(a * b * 100 / c))
        print(lado)

