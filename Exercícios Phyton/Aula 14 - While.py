'''for c in range(1,10):
    print(c)
print('FIM')'''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print('Foi digitado {} números pares e {} números ímpares'.format(par, impar))
