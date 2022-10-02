
sexo = str(input('Digite o sexo (F/M): ')).strip().upper()[0]

while sexo not in 'FM':
   sexo = str(input('Dados inválidos. Por favor,g digite novamente o sexo (F/M): ')).strip().upper()[0]

print('Sexo {} registrado com sucesso!'.format(sexo))