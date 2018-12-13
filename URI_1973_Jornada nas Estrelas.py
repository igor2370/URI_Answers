n = int(input())
x = list(map(int, input().split()))

carneiro = sum(x)
estrela = 0

par = False

for i in x:
    estrela += 1
    if i % 2 == 0:
        par = True
        break

for i in range(n):
    if x[i] > 0:
        x[i] = x[i] - 1
        if i % 2 == 0:
            break

cont_zero = x.count(0)

if par == False:
    carneiro = carneiro - estrela
else:
    carneiro = carneiro - (2 * estrela - 1) + cont_zero


print('{1} {0}'.format(carneiro, estrela))
