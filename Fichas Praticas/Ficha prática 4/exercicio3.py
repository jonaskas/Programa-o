"""
Exercicio 3
"""



def lerInteiro(min, max):
    numero = min - 1
    while numero < min or numero > max:
        numero = int(input('Introduza um numero: '))
    return numero
numero = lerInteiro(0, 20)


print(numero)