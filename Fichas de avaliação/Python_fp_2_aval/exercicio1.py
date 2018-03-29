"""
Exercico 1
"""


print ('\n\nAs Notas devem ser todas de (0 a 20)')

#-----------Nota 1-----------

nota1 = float(input('\nIntroduza a 1ª Nota: '))
while nota1 < 0.0 or nota1 > 20.0:
    nota1 = float(input('Introduza a 1ª Nota: '))    

#-----------Nota 2-----------

nota2 = float(input('Introduza a 2ª Nota: '))    
while nota2 < 0.0 or nota2 > 20.0:
    nota2 = float(input('Introduza a 2ª Nota: '))

#-----------Nota 3-----------

nota3 = float(input('Introduza a 3ª Nota: '))    
while nota3 < 0.0 or nota3 > 20.0:
    nota3 = float(input('Introduza a 3ª Nota: '))

#-----------Media das notas-----------    

media = float((nota1 * .25 + nota2 * .35 + nota3 * .40))

if media >= 9.5 :
    resultado = "Aprovado\n"
else:
    resultado = "Reprovado\n"

print('\nMedia = {}\nResultado = {}'.format(media, resultado))
