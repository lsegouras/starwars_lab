from random import randint
jogador = soma = vitoria = 0
opcao = ''


print("---------------------------")
print(" VAMOS JOGAR PAR OU ÍMPAR")
print("---------------------------")

while True:
 jogador = int(input('Digite um número de 1 a 10: '))
 opcao = str(input('Par ou Ímpar P/I? ')).strip().upper()
 computador = randint(0,10)
 soma = jogador + computador

 print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {soma}.')
 print('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')

 if opcao == 'P':
  if soma % 2 == 0:
   print('Você venceu!')
   vitoria += 1
  else:
   print('Você perdeu!')
   break

 elif opcao == 'I':
  if soma % 2 == 1:
   print('Você venceu!')
   vitoria += 1
  else:
   print('Você perdeu!')
   break
 print('Vamos jogar novamente!')

print(f'Game Over! Você venceu {vitoria} vezes ')

