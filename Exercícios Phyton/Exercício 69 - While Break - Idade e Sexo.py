idade = maiorDezoito = numHomens = fMenorVinte = 0
sexo = ''
continuar = ''


while True:
    print("---------------------")
    print(" CADASTRE UMA PESSOA")
    print("---------------------")
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo M/F: ')).strip().upper()

    if idade > 18:
        maiorDezoito += 1

    if sexo == 'M':
        numHomens += 1

    if sexo == 'F' and idade < 20:
        fMenorVinte +=1

    continuar = str(input('Quer continuar S/N? ')).strip().upper()

    if continuar == 'N':
        break

print(f'O número de pessoas com mais de 18 anos é {maiorDezoito}')
print(f'O número de homens é de {numHomens}')
print(f'O número de mulheres com menos de 20 anos são {fMenorVinte}')

print('Volte sempre!')





