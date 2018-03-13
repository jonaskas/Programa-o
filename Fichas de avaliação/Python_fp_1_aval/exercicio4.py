"""
Exercicio 4
"""
nota1 = float(input('\nIntroduza a 1ª Nota: '))
nota2 = float(input('Introduza a 2ª Nota: '))
nota3 = float(input('Introduza a 3ª Nota: '))

media = float((nota1 * 25 + nota2 * 35 + nota3 * 40)//100)
media_inteira = int(media)
media_modulo = (nota1 * 25 + nota2 * 35 + nota3 * 40)%100

print('\nMedia = {}\nMedia Inteira = {}\nMedia Modulo = {} \n'.format(media,media_inteira,int(media_modulo)))

