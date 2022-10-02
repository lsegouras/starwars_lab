

f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(inverso)

if inverso == junto:
    print('A frase {} é um palíndromo.'.format(f))
else:
    print('A frase {} não é um palíndromo.'.format(f))

