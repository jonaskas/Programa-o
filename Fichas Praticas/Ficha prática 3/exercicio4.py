"""
Exercico 4
"""

tabuada = int(input("Introduza a numero tabuada que deseja saber: "))

x = 1

while x <= 10:
    resultado = tabuada * x
    print("{} * {} = {}".format(tabuada, x, resultado))
    x += 1  