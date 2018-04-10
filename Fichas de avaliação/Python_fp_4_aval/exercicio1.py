"""
Exxercicio 1
"""
def login(user_test, password_test):
    user = "aluno"
    password = "Estg2018"
    if user_test == user and password_test == password:
        return True
    return False


def validarlogin():
    contador = 0
    while contador < 3:
        contador += 1
        user_test = input('Utilizador: ')
        password_test = input('Password: ')
        if login(user_test, password_test):
            print('Login efetuado com sucesso.')
            break
        else:
            print('\nLogin nao foi efetuado com sucesso\n')
validarlogin()