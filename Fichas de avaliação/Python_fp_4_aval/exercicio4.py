"""
Exxercicio 4
"""

def imprimir(n):
    if n > 0:
       imprimir(n -1)

    print(n,end=" ")
    
numero = int(input('Introduza um numero: '))

imprimir(numero)


