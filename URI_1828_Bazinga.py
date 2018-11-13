d1 = {'pedra':'1', 'papel':'2', 'tesoura':'3', 'lagarto':'4', 'Spock':'5'}
v = 'Bazinga!'
e = 'De novo!'
d = 'Raj trapaceou!'
d2 = {'11':e,'12':d,'13':v,'14':v,'15':d,'21':v,'22':e,'23':d,'24':d,'25':v,'31':d,'32':v,'33':e,'34':v,
      '35':d,'41':d,'42':v,'43':d,'44':e,'45':v,'51':v,'52':d,'53':v,'54':d,'55':e}

t = int(input())

for i in range(1,t+1):
    c, r = input().split()
    caso = d1[c]+d1[r]
    print('Caso #{}: {}'.format(i,d2[caso]))
