nTermos = int(input('Digite o número de termos que deseja obter na PA: '))
pTermo = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1
print('Os {} primeiros termos da PA são: '.format(nTermos, end=''))

while c < nTermos:
    print('{}, '.format(pTermo), end='')
    pTermo += r
    c += 1
print(pTermo)