N=eval(input())
N=float('%.2f' % N)
l=[100,50,20,10,5,2,1,0.5,0.25,0.1,0.05,0.01]
resp=[]
t=0
for i in l:
    temp = int(N/i)
    resp.append(temp)
    N-=i*temp
    N = float('%.2f' % N)
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(resp[0]))
print('{} nota(s) de R$ 50.00'.format(resp[1]))
print('{} nota(s) de R$ 20.00'.format(resp[2]))
print('{} nota(s) de R$ 10.00'.format(resp[3]))
print('{} nota(s) de R$ 5.00'.format(resp[4]))
print('{} nota(s) de R$ 2.00'.format(resp[5]))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(resp[6]))
print('{} moeda(s) de R$ 0.50'.format(resp[7]))
print('{} moeda(s) de R$ 0.25'.format(resp[8]))
print('{} moeda(s) de R$ 0.10'.format(resp[9]))
print('{} moeda(s) de R$ 0.05'.format(resp[10]))
print('{} moeda(s) de R$ 0.01'.format(resp[11]))
