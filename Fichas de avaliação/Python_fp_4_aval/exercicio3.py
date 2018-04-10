"""
Exxercicio 3
"""
def figura(linhas, colunas, caracter) :
     
    for i in range(1, linhas + 1) :
        for j in range(1, colunas + 1) :
            if (i == 1 or i == linhas or j == 1 or j == colunas) :
                print(caracter, end="")            
            else :
                print(" ", end="")            
        print()
 
 
linhas = int(input('Quantas linhas deseja: '))
colunas = int(input('Quantas colunas deseja: '))
caracter = input('Escolha o caracter do desenho: ')


figura(linhas, colunas, caracter)      

