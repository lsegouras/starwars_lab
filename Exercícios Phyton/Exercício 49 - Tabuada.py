cont = 0
mult = 0
n = int(input('Digite um número que deseja obter a tabuada: '))
for c in range (1, 11, 1):
    cont = cont + 1
    mult = cont * n
    print('{} X {:2} = {}'.format(n, cont, mult))
