"""
Exercicio 5
"""


resultado = 0
contar = 0
soma = 0
while True: 
    numero=int(input('Introduza um valor: '))
    if numero == -1 :
        break

    contar = contar + 1
    soma = soma + numero
    
    if contar != 0 :
        resultado = soma / contar
print("Muito bem!\nA média de numeros que inserieste é de: ",resultado)