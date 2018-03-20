"""
Exercicio 3
"""

limite = int(input("Introduza um numero inteiro: "))
salto = int(input("Introduza um numero para o salto : "))


print("\nValores lidos: ")
for i in range(0, limite+1, salto):
    print(i, end=" ")
