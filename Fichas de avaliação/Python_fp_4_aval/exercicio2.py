"""
Exxercicio 2
"""
euro = 1.231
dolar = 0.8089

def convertor_euro(quantidade):
    return (quantidade * euro) / 1

def convertor_dolar(quantidade):
    return (quantidade * dolar) / 1

def teste():
    escolha = input("Introduza em que moeda queres converter €(E) ou $(D): ")
    quantidade = float(input('Introduza uma quantidade: '))
    if escolha == 'E':
        print ('{}€ sao {}$'.format(quantidade, convertor_euro(quantidade)))
    elif escolha == 'D':
        print ('{}$ sao {}€'.format(quantidade, convertor_dolar(quantidade)))

teste()