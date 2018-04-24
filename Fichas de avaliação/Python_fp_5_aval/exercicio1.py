"""
Exercicio 1
"""
from random import randint
import time
import re
"""
def isValidEmail(email):
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
        return False
if isValidEmail("my.email@gmail.com") == True :
    print("This is a valid email address")
else:
    print("This is not a valid email address")
"""
class Utilizador():

    def __init__(self):
        self.nome = None
        self.email = None
        self.password = None
        self.id = None
        self.bloquear = False
        self.resp_secreta = None
        self.data_criacao = None
        self.ultimo_login = None
        
        


person1 = Utilizador()
print("Utilizador 1:")
person1.nome = input("Introduza o nome do utilizador: ")
person1.email = input("Introduza o email : ")
person1.password = input("Introduza uma password : ")
person1.id = "{}-{}".format(randint(100, 999),randint(1000, 9999))
person1.data_criacao = time.strftime("%d/%m/%Y")
person1.resp_secreta = input("Qual é o nome do teu primeiro cão?\nResposta: ")

person2 = Utilizador()
print("\n\nUtilizador 2:")
person2.nome = input("Introduza o nome do utilizador: ")
person2.email = input("Introduza o email : ")
person2.password = input("Introduza uma password : ")
person2.id = "{}-{}".format(randint(100, 999),randint(1000, 9999))
person2.data_criacao = time.strftime("%d/%m/%Y")
person2.resp_secreta = input("Qual é o nome do teu primeiro cão?\nResposta: ")  


print("\n"*3)



def login(email_test, password_test):
    if email_test ==  person.email and password_test == person.password:
        return True
    return False


def validarlogin():
    contador = 0
    while contador < 3:
        contador += 1
        email_test = input('Email: ')
        password_test = input('Password: ')
        if self.bloquear == False:
            if login(email_test, password_test):
                print('Login efetuado com sucesso.')
                menulogin()
                break
            else:
                print('\nLogin nao foi efetuado com sucesso\n')
        else:
            print("Resposta de segurança!")
            pre_segurnca = input("Qual é o nome do teu primeiro cão?: ")
            if pre_segurnca == self.resp_secreta
    else:
        self.bloquear = True
        validarlogin()


def menulogin():
    print("*"*25)
    print("1-Dados Utilizador")
    print("2-Mudar Utilizador")
    print("*"*25)
    resposta = input("Resposta:")
    if resposta == 1:
        def __str__(self):
            return "Nome: {}\nemail: {}\npassword: {}\nID: {}\nBloaquedo: {}\nResposta Secreta: {}\nData de Criação: {}\nData do ultimo login: {}".format(self.nome, self.email, self.password, self.id, self.bloquear, self.resp_secreta, self.data_criacao, self.ultimo_login)
        elif resposta == 2:
            validarlogin()
        

print(menulogin())
"""
print(person)
validarlogin()
"""