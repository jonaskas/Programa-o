"""
Exercicio 4
"""
numero = int(input('Intoduza um numero: '))

div3 = numero % 3
div5 = numero % 5

if div3 == 0 and div5 == 0 :
    print ('O número {} é divisivel por 3 e por 5'.format(numero))
elif div3 != 0 and div5 != 0 :
    print ('O número {} não é divisivel por 3 nem por 5'.format(numero))  
elif div3 == 0 and div5 != 0 :
    print ('O número {} é divisivel por 3 mas não por 5'.format(numero))
elif div3 != 0 and div5 == 0 :
    print ('O número {} não é divisivel por 3 mas sim por 5'.format(numero))