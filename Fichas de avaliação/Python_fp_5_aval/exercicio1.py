"""
Exercicio 1
"""
from random import randint
import time
import re


'''
def isValidEmail(email):
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
        return False
if isValidEmail("my.email@gmail.com") == True :
    print("This is a valid email address")
else:
    print("This is not a valid email address")
'''


class Utilizador():
    def __init__(self):
        self.nome = None
        self.email = None
        self.password = None
        self.id = None
        self.bloquear = None
        self.resp_secreta = None
        self.data_criacao = None
        self.ultimo_login = None    



def validarlogin(self):
    contador = 0
    while contador < 3:
        email_test = input('Email: ')
        password_test = input('Password: ')
        if self.bloquear == False:
            if login(email_test, password_test):
                print('Login efetuado com sucesso.')
                menu_utilizador(self)   
            else:
                print('\nLogin nao foi efetuado com sucesso\n')
                contador += 1
        else:
            print("Resposta de segurança!")
            pre_segurnca = input("Qual é o nome do teu primeiro cão?\nResposta: ")
            if pre_segurnca == self.resp_secreta:
                self.bloquear == False
                validarlogin(self)
    else:
        self.bloquear = True
        validarlogin(self)



def login(email_test, password_test):
    if email_test == (person1.email or person2.email) and password_test == (person1.password or person2.password):
        return True
    return False



def menu_utilizador(self):
    print("*"*25)
    print("1-Dados Utilizador")
    print("2-Mudar Utilizador")
    print("*"*25)
    resposta = input("Resposta:")
    if resposta == 1:
        return "Nome: {}\nemail: {}\npassword: {}\nID: {}\nBloaquedo: {}\nResposta Secreta: {}\nData de Criação: {}\nData do ultimo login: {}".format(self.nome, self.email, self.password, self.id, self.bloquear, self.resp_secreta, self.data_criacao, self.ultimo_login)
   



person1 = Utilizador()
print("Utilizador 1:")
person1.nome = input("Introduza o nome do utilizador: ")
person1.email = input("Introduza o email : ")
person1.password = input("Introduza uma password : ")
person1.id = "{}-{}".format(randint(100, 999),randint(1000, 9999))
person1.data_criacao = time.strftime("%d/%m/%Y")
person1.resp_secreta = input("Qual é o nome do teu primeiro cão?\nResposta: ")
person1.bloquear = False



person2 = Utilizador()
print("\n\nUtilizador 2:")
person2.nome = input("Introduza o nome do utilizador: ")
person2.email = input("Introduza o email : ")
person2.password = input("Introduza uma password : ")
person2.id = "{}-{}".format(randint(100, 999),randint(1000, 9999))
person2.data_criacao = time.strftime("%d/%m/%Y")
person2.resp_secreta = input("Qual é o nome do teu primeiro cão?\nResposta: ")  
person2.bloquear = False
print("\n"*3)
print validarlogin()

