"""
Exercicio 2
"""
def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    return numero1 / numero2



numero1 = int(input('Introduza um 1º numero: '))
numero2 = int(input('Introduza um 2º numero: '))

operacao = input('Escolha uma função(+),(-),(*),(/): ')

if operacao == "+":
    print('{} + {} = {}'.format(numero1,numero2,soma(numero1,numero2)))
elif operacao == "-":
     print('{} - {} = {}'.format(numero1,numero2,subtracao(numero1,numero2)))
elif operacao == "*":
    print('{} * {} = {}'.format(numero1,numero2,multiplicacao(numero1,numero2)))
elif operacao == "/":
    print('{} / {} = {}'.format(numero1,numero2,divisao(numero1,numero2)))
