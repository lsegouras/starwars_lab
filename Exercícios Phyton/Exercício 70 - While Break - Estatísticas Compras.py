
print('--------------------------')
print(' SUPERMERCADO BEM BARATO')
print('--------------------------')

total = maior1000 = contador = 0
continuar = ''
menor = 0
maisBarato = ''

while True:
    nomeProduto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$ '))
    total += preco
    contador += 1
    if preco >= 1000:
        maior1000 += 1
    if contador == 1 or preco < menor:
        menor = preco
        maisBarato = nomeProduto

    continuar = str(input('Deseja continuar o cadastro [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f'O total gasto foi de R$ {total}.')
print(f'{maior1000} produtos custaram mais que R$1000,00')
print(f'O produto com menor preço foi {maisBarato} com o valor de R${menor: .2f}')
