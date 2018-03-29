"""
Exercicio 1
"""
numero = int(input('Introduza um numero: '))

print('Os 5 numeros anteriores a {}'.format(numero))
for i in range(numero -1, numero -6, -1):
    print(i, end=" ")
    
print('\nOs 5 numeros seguintes a {}'.format(numero))    
for o in range(numero +1, numero +6, 1):
    print(o, end=" ")

