"""
Exercicio 1
"""
import re

def isValidEmail(email):
    if len(email) > 7:
    if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
    return True
    return False
if isValidEmail("my.email@gmail.com") == True :
    print "This is a valid email address"
else:
    print "This is not a valid email address"

print('Resgisto:\n ')

Nome = input('Nome: ')
email = input('Email: ')
password = input('Password: ')
cc = input('Cartão de cidadão: ')
Resp_Secreta = input('Qual é o nome do teu primeiro cão?\nResposta: ')
