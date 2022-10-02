somaIdade = 0
media = 0
maisVelho = 0
nomeMaisVelho = ''
menosVinte = 0

for c in range(1,5):
    print('----- {}º PESSOA -----)'.format(c))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = int(input('Digite (1) se for do sexo feminino e (2) se for do sexo masculino: '))
    somaIdade = somaIdade + i

    if c == 1 and s == 2:
        maisVelho = i
        nomeMaisVelho = n
    if i > maisVelho and s == 2:
        maisVelho = i
        nomeMaisVelho = n

    if s == 1 and i < 20:
        menosVinte = menosVinte + 1

media = somaIdade / 4
print('A média de idade do grupo é de {}.'.format(media))
print('O homem mais velho tem {} anos e o nome dele é {}.'.format(maisVelho, nomeMaisVelho))
print('{} mulheres tem menos de 20 anos'.format(menosVinte))














