salario=input()
salario=float('{:.2f}'.format(eval(salario)))

if (salario-4500)<=0:
    ir28=0
else:
    ir28=(salario - 4500)*0.28
    salario=4500

if (salario-3000)<=0:
    ir18=0
else:
    ir18=(salario - 3000)*0.18
    salario=3000

if (salario-2000)<=0:
    print('Isento')
else:
    ir8=(salario - 2000)*0.08
    ir=ir8+ir18+ir28
    print('R$ {:.2f}'.format(ir))
