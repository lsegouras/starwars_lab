from datetime import date
agora = date.today().year
idade = 0
somaMaior = 0
somaMenor = 0
for c in range(1, 4):
    ano = int(input('Digite seu ano de nascimento (4 dígitos): '))
    idade = agora - ano
    if idade >= 18:
        somaMaior = somaMaior + 1
    else:
        somaMenor = somaMenor + 1
print("O número de pessoas que já atingiram a maioridade é {}".format(somaMaior))
print("O número de pessoas que ainda não atingiram a maioridade é {}".format(somaMenor))