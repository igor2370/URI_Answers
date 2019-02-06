case = 1
while 1:
    try:
        n1 = input()
        n2 = input()
        qtd = n2.count(n1)
        pos = n2.rfind(n1)+1
        print('Caso #{}:'.format(case))
        if qtd == 0:
            print('Nao existe subsequencia')
            print()
        else:
            print('Qtd.Subsequencias: {}'.format(qtd))
            print('Pos: {}'.format(pos))
            print()
        case += 1
    except EOFError:
        break
