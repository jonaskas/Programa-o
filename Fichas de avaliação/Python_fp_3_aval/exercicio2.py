"""
Exercicio 2
"""

numero = int(input('Introduza um numero para confirmar se é primo ou não: '))

if numero == 2:
    print('O número {} é primo'.format(numero))
else:
    while numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                print('O número {} não é primo'.format(numero))
                break
            else:
                print('O número {} é primo'.format(numero))
                break
        break

if numero <= 1:
    print('Para ser considerado numero primo tem de ser um numero superior a 1!')   