"""
Exercicio 3
"""
massa = float(input('Introduza o seu peso: '))
altura = float(input('Introduza o sua altura: '))

alt = altura ** 2
imc = massa / alt

print('O seu Indicede massa corporal é de {}'.format(imc))