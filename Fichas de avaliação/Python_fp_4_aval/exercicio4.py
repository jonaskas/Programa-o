"""
Exxercicio 4
"""

def imprimir(n):
    if n == -1:
        return 0
    elif imprimir(n -1):
        return n 
    print(n)

numero = int(input('Introduza um numero: '))

imprimir(numero)


