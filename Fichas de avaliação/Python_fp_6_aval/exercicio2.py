"""
Exercicio 2
"""
def  quantidade(carater):  
    teste = input('Introduza 1 caratere: ')
    contar = carater.count(teste)
    print("A letra {} existe: {} vezes.".format(teste, contar)) 
    for i,j in enumerate(carater):
        if j == teste:
            print("A letra {} encontra-se na posição {}.".format(j,i))

carater = []
x = 1
while x <= 10:
    c = input('Digite um carater: ')
    carater.append(c)
    x += 1


quantidade(carater)