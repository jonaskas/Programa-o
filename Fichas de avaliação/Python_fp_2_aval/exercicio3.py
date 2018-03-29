"""
Exercicio 3
"""

numero = int(input('Introduza um número: '))

resultado = numero % 2
if resultado == 0 :
     print("O número {} é par".format(numero))
else:
    print("O número {} é ímpar".format(numero))
