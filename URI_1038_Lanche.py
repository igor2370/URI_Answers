cod,qtd=input().split()
cod=int(cod)
qtd=int(qtd)
prod={1:4,2:4.5,3:5,4:2,5:1.5}
total=prod[cod]*qtd
print('Total: R$ {:.2f}'.format(total))
