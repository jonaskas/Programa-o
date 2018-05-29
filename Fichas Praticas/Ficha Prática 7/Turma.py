"""
Exercicio 1
Turma
"""
import aluno from Aluno

class Turma():
    
    def __init__(self, nome ,numero ,ano, alunos, total_alunos):
        self.aluno = nome
        self.numero = numero
        self.ano = ano 
        self.total_alunos = 0
        self.alunos = []

    def verificar_se_existe(self,aluno):
        for i in range(self.total_alunos):
            if self.alunos[i].a.igual(aluno):
                return True 
        return False
    def inserir_instancia_aluno(self, aluno):
        if self.verificar_se_existe(aluno) == False:
            self.alunos.append(aluno)
            self.total_alunos += 1
            return True
        return False

    def insere_aluno(self, numero, nome):
        aluno = Aluno(numero, nome)
        return self.inserir_instancia_aluno(self, aluno)









    




turmas = "CRSIT2"
ano_letivo = 2018 
turma = (turmas, ano_letivo)