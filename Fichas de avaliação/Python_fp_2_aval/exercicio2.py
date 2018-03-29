"""
Exercicio 2
"""
primeiro_numero = int(input('Introduza o primeiro numero: '))
segundo_numero = int(input('Introduza o segundo numero: '))
terceiro_numero = int(input('Introduza o terceiro numero: '))


if primeiro_numero > segundo_numero and segundo_numero > terceiro_numero : # 1 > 2 > 3
    print('{} > {} > {}' .format(primeiro_numero, segundo_numero, terceiro_numero)) 

elif primeiro_numero > terceiro_numero and terceiro_numero > segundo_numero : # 1 > 3 > 2
     print('{} > {} > {}' .format(primeiro_numero, terceiro_numero, segundo_numero)) 

elif segundo_numero > primeiro_numero  and primeiro_numero > terceiro_numero : # 2 > 1 > 3
     print('{} > {} > {}' .format(segundo_numero, primeiro_numero, terceiro_numero)) 

elif segundo_numero > terceiro_numero and terceiro_numero > primeiro_numero : # 2 > 3 > 1
     print('{} > {} > {}' .format(segundo_numero, terceiro_numero, primeiro_numero)) 

elif terceiro_numero > primeiro_numero and primeiro_numero > segundo_numero : # 3 > 1 > 2
     print('{} > {} > {}' .format(terceiro_numero, primeiro_numero, segundo_numero)) 

elif terceiro_numero > segundo_numero and segundo_numero > primeiro_numero : # 3 > 2 > 1
     print('{} > {} > {}' .format(terceiro_numero, segundo_numero, primeiro_numero)) 
     
