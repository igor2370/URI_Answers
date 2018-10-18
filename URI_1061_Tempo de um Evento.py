diaInicial=input()
diaInicial=int(diaInicial[4:])
horaInicial=input()
diaFinal=input()
diaFinal=int(diaFinal[4:])
horaFianl=input()
h1=int(horaInicial[:2])
m1=int(horaInicial[5:7])
s1=int(horaInicial[10:])
h2=int(horaFianl[:2])
m2=int(horaFianl[5:7])
s2=int(horaFianl[10:])
inicio=diaInicial*24*60*60+h1*60*60+m1*60+s1
fim=diaFinal*24*60*60+h2*60*60+m2*60+s2
tempo=fim-inicio
dia=tempo//86400
hora=(tempo%86400)//3600
minuto=((tempo%86400)%3600)//60
segundo=((tempo%86400)%3600)%60
print('{} dia(s)'.format(dia))
print('{} hora(s)'.format(hora))
print('{} minuto(s)'.format(minuto))
print('{} segundo(s)'.format(segundo))
