while 1:
    try:
        n = int(input())
        for i in range(n):
            vet = ''
            for j in range(n):
                if (i + j)==n-1:
                    vet+='2'
                elif i == j:
                    vet += '1'
                else:
                    vet += '3'
            print(vet)

    except EOFError:
        break
