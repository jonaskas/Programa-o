"""
Exercicio 1
"""
from random import randint
Numero_Vezes = 10

file = open("Fichas de avaliação\Python_fp_7_aval\dados.txt", "a")

for i in range(Numero_Vezes):
    a = str(randint(0, 9)) + "\n"
    file.write(a)
    #print(a, end=" ")

file.close()


