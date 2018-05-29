"""
Exercicio 1
Aluno
"""
class Aluno():

    def __init__(self,numero, nome):
        self.numero = numero
        self.nome = nome

    def __str__(self):
        return "Numero: {} | Nome: {}".format(self.numero, self.nome.title())
    


A1 = Aluno(1, "Joaquim")
print(A1)

A2 = Aluno(2, "miguel")
print(A2)


