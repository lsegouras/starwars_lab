valor = cont = c = m = 0

while True:
    valor = int(input('Deseja ver a tabuada de qual valor: '))

    if valor < 0:
        break

    for cont in range(1,11,1):
        c += 1
        m = valor * c
        print(f'{valor} X {c} = {m}')

print('Volte sempre!')