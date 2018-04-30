"""
Exercicio 3
"""
def conteudo_da_lista(myList):
    for i in range(len(myList)):
        print(myList[i],end=" ")

def dobro(myList):
    for i in range(len(myList)):
        print(myList[i]*2,end=" ")

def soma(myList):
    sum = 0
    for numeros in myList:
        sum += numeros
    return sum 

def media(myList):
    sum = 0
    for numeros in myList:
        sum += numeros
    return sum /len(myList)

numeros = []
x = 1
while x <= 20:
    n = int(input('Digite um número: [ %s ]: '%x))
    numeros.append(n)
    x += 1


print('\nConteúdo da lista:') 
conteudo_da_lista(numeros)
print('\nDobro de cada elemento:') 
dobro(numeros)
print('\n\nSoma da lista:', soma(numeros))
print('\nMedia da lista:', media(numeros))
print("\nMaior número da lista é:", max(numeros))
print("\nMenor número da lista é:", min(numeros))