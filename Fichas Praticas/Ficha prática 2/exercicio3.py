"""
Exercicio 3
"""

primeiro = float(input('Insira o 1º Numero: '))
segundo = float(input('Insira o 2º Numero: '))
operacao = input('+ Soma\n/ Divisão\n- Subtração\n* Multiplicação\n')

if operacao == '+':
    resultado = primeiro + segundo
elif operacao == '/':
    resultado = primeiro / segundo
elif operacao == '-':
    resultado = primeiro - segundo
elif operacao == '*':
    resultado = primeiro * segundo
else:
     resultado = "Invalido"

print(resultado) 
    