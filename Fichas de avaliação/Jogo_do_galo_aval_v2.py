"""
Jogo do Galo
"""
import os
import csv
from pathlib import Path


class Tabuleiro():

    def __init__(self):
        self.lista = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
    
    def __str__(self):
        cima = "  A|B|C|"
        for i in range (0, 3):
            cima += "\n" + str(i+1) + "|"
            for j in range(0, 3):
                if self.lista[i][j] == None:
                    cima += " |"
                else:
                    cima += self.lista[i][j] + "|"
        return cima
    
    def validarjogada(self, jogada, token):        
        if (jogada[0] == "A" or jogada[0] == "B" or jogada[0] == "C") and (jogada[1] == "1" or jogada[1] == "2" or jogada[1] == "3"):

            if jogada[0] == "A":
                coluna = 0
            if jogada[0] == "B":
                coluna = 1 
            if jogada[0] == "C":
                coluna = 2  

            linha = int(jogada[1]) - 1

            if self.lista[linha][coluna] == None:
               self.lista[linha][coluna] = token   
            else:
                print("Jogada Inválida!")
                jogada = input("Tente 1Outravez!\n>> ")
                self.validarjogada(jogada,token)
        else:
            print("Jogada Inválida!")
            jogada = input("Tente 2Outravez!\n>> ")
            self.validarjogada(jogada,token)

    def ver(self, token):
        if  (self.lista[0][0] == token and self.lista[0][1] == token and self.lista[0][2] == token) or \
            (self.lista[1][0] == token and self.lista[1][1] == token and self.lista[1][2] == token) or \
            (self.lista[2][0] == token and self.lista[2][1] == token and self.lista[2][2] == token) or \
            (self.lista[0][0] == token and self.lista[1][0] == token and self.lista[2][0] == token) or \
            (self.lista[0][1] == token and self.lista[1][1] == token and self.lista[2][1] == token) or \
            (self.lista[0][2] == token and self.lista[1][2] == token and self.lista[2][2] == token) or \
            (self.lista[0][0] == token and self.lista[1][1] == token and self.lista[2][2] == token) or \
            (self.lista[2][0] == token and self.lista[1][1] == token and self.lista[0][2] == token):
            return True
        return False


class jogador():
    
    def __init__(self):
        self.nome = None
        self.token = None
    
    
"""

def write_CSV(filepath, data, delim = ","):
    with open(filepath, "w", newline='') as file:
        writer = csv.writer(file, delimiter=delim)
        for line in data:
            writer.writerow(line)

def write_CSV_DICT(filepath, data, headers, delim = ","):
    with open(filepath, "w", newline='') as file:
        writer = csv.DictWriter(file, delimiter=delim, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def read_CSV(filepath, delim = ",") :
    with open(filepath, "r") as file:
        data = csv.reader(file, delimiter=delim)
        for row in data:
            print("\t".join(row))

if __name__ == "__main__":

    filePath = "Fichas de avaliação\Trabalho_Final\dados.txt"

    Jogadores = []

    write_CSV(filePath, Jogadores)
    read_CSV(filePath)

    # Creates dict
    header = ["Nome", "Token", "Pontuação", "Jogos Realizados"]
    NovosJogadores = [dict(zip(header, row)) for row in Students]
    print( "\n".join([str(row) for row in NovosJogadores]))

    print()
    write_CSV_DICT(filePath, NovosJogadores, header)
    read_CSV(filePath)
   """  
###################
t = Tabuleiro()
j1 = jogador
j2 = jogador
j1.nome = "João"
j1.token = "X"
j2.nome = "Filipe"
j2.token = "O"
#################


for x in range (0, 5):
  
    print(t)
    jogada = input("Escolha as coordenadas!\nSe quiser desistir pressione a tecla 9.\n>>  ")
    if jogada == "9":
        print("O {} desistiu!! \nO venncedor é o {}. ".format(j1.nome, j2.nome))
        break
    else:  
        if t.ver(j1.token) == True:
            print("O vencedor é ", j1.nome)
            break
        else:
            t.validarjogada(jogada, j2.token)
            print(t)
        
        if t.ver(j2.token) == True:
            print("O vencedor é ", j2.nome)
            break
        else:
            t.validarjogada(jogada, j1.token)
            print(t)

        if x == 5:
            print("Empate")
            break
    

