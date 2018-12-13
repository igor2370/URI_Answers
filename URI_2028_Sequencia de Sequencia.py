caso = 1

while 1:
    try:
        cont = 1
        n = int(input())
        if n > 0:
            l = '0 '
        else:
            l = '0'
        for i in range(n + 1):
            for j in range(i):
                if i == n and j == n - 1:
                    l += str(i)
                else:
                    l += str(i) + ' '
                cont += 1

        if n == 0:
            print('Caso {}: {} numero'.format(caso, cont))
        else:
            print('Caso {}: {} numeros'.format(caso, cont))

        print(l)
        print()

        caso += 1


    except EOFError:
        break
