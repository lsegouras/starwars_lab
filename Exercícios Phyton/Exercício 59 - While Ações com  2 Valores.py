v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o primeiro valor: '))
opcao = 0
s = 0
m = 0
maior = 0

while opcao != 5:
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')

    opcao = int(input('Digite o número correspondente ao que deseja fazer: '))

    if opcao == 1:
        s = v1 + v2
        print('A soma dos números {} e {} é {}.'.format(v1, v2, s))
    elif opcao == 2:
        m = v1 * v2
        print('A multiplicação dos números {} e {} é {}.'.format(v1, v2, m))
    elif opcao == 3:
        maior = v1
        if v2 > maior:
            maior = v2
        print('O número maior é {}.'.format(maior))
    elif opcao == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o primeiro valor: '))
    elif opcao == 5:
        print('Fim do programa!')
    else:
        print('Opção inválida! Digite novamente!')







