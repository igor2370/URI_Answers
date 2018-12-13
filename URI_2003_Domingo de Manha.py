while 1:
    try:
        h, m = map(int, input().split(':'))

        if h < 7 or (h == 7 and m == 0):
            print('Atraso maximo: 0')
        else:
            print('Atraso maximo: {}'.format(((h+1)-8)*60 + m))

    except EOFError:
        break
