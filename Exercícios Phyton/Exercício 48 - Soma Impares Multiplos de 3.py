m = 0
s = 0
for c in range(1, 501, 2):
    print(c)
    m = c % 3
    if(m == 0):
        s = s + c
print('A somatória dos números ímpares, múltiplos de 3, é {}'.format(s))
