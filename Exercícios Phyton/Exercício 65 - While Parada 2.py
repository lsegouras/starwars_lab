media = soma = cont = maior = menor =0
res = 'S'

while res == 'S':
    n = int(input('Digite outro número inteiro: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    res = str(input('Deseja digitar outro número? [S ou N] ')).upper().strip()[0]

media = soma / cont
print('Você digitou {} números e a média foi {}. O maior número foi {} e p menor foi {}'.format(cont,media, maior, menor))





