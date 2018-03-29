"""
Exercicio 5
"""
saldo = float(input('Introduza o valor do seu saldo bancario: '))

#Tabela
print('\n\n*************************')
print('*   1-Creditar saldo    *')
print('*                       *')
print('*   2-Debitar saldo     *')
print('*************************\n\n')

operacao = int(input('Escolha se quer Creditar ou Debitar: '))
montante = float(input('Montante: '))

# 1 Operação

if operacao == 1 :
    novosaldo = saldo + montante
    print('Credito realizado com sucesso!')
    print('Saldo da conta é de {} €'.format(novosaldo))

# 2 Operação

if operacao == 2 :
    novosaldo = saldo - montante
    if novosaldo < 0 :
        print('Operação impossivel, saldo insuficiente.')
    else:
        print('Débito realizado com sucesso!')
        print('Saldo da conta é de {} €'.format(novosaldo))    

