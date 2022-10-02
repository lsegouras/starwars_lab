import random
import time

c = 0
palpite = 1
computador = random.randint(1,10)
print('Sou seu computador! Pensei em um número de 1 a 10! Consegue acertar?')
time.sleep(3)

while computador != palpite:
    palpite = int(input('Digite seu palpite: '))
    c = c + 1

print('Você acertou! Pecisou de {} tentativas para acertar!'.format(c))





