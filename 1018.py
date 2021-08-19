valor = temp = int(input())
lista = [100, 50, 20, 10, 5, 2, 1]
notas = [0, 0, 0, 0, 0, 0, 0]

for i in range(0, len(lista)):
    if temp//lista[i] > 0:
        notas[i] = temp//lista[i]
        if temp % lista[i] == 0:
            break
        else:
            temp = temp % lista[i]

print(valor)
for j in range(0,len(lista)):
    print(f'{notas[j]} nota(s) de R$ {lista[j]},00')
