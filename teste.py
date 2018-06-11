import os
import csv
from pathlib import Path

class Jogador():
    
    def __init__(self, nome, token, pontuaçao, jogos): #A semelhança nesta classe com a dos meu colegas Diogo Neves e Carlos Antunes foi porque me ajudaram a difinir as classes        
        self.nome = nome
        self.token = token
        self.pontuaçao = pontuaçao
        self.jogos = jogos

class Tabuleiro():

    def __init__(self):
        self.tabuleiro = [[None, None , None ], 
                          [None, None , None ], 
                          [None, None , None ]]
    
    def __str__(self):
        l1 = ' {} | {}  | {}  '.format(self.tabuleiro[0][0], self.tabuleiro[0][1], self.tabuleiro[0][2])
        l2 = ' {} | {}  | {}  '.format(self.tabuleiro[1][0], self.tabuleiro[1][1], self.tabuleiro[1][2])
        l3 = ' {} | {}  | {}  '.format(self.tabuleiro[2][0], self.tabuleiro[2][1], self.tabuleiro[2][2])
        l4 = '----------------'
        s = '\n'.join([l1, l4, l2, l4, l3])
        return s
    
    #Função que nos permite verificar a jogada inserida pelo o jogador e inserir a mesma na lista
    def validar_jogada(self,jogada,token):
        if (jogada[0] == "A" or jogada[0] == "B" or jogada[0] == "C") and (jogada[1] == "1" or jogada[1] == "2" or jogada[1] == "3"):
            coluna = None
            if jogada[0] == "A":
                coluna = 0
            if jogada[0] == "B":
                coluna = 1
            if jogada[0] == "C":
                coluna = 2
            linha = int(jogada [1]) - 1
            if self.tabuleiro[linha][coluna] == None:
                self.tabuleiro[linha][coluna] = token
                return True
            else:
                return False
        else:
            return False
    
    #Função que permite verificar se existe vencedor do jogo
    def vencedor(self,token): #A semelhança de termos separados as opçãos por linhas em vez de uma só deve-se à ajuda do João Gonçalves 
        if  (self.tabuleiro[0][0] == token and self.tabuleiro[0][1] == token and self.tabuleiro[0][2] == token) or \
            (self.tabuleiro[1][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[1][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[2][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[0][0] == token and self.tabuleiro[1][0] == token and self.tabuleiro[2][0] == token) or \
            (self.tabuleiro[0][1] == token and self.tabuleiro[1][1] == token and self.tabuleiro[2][1] == token) or \
            (self.tabuleiro[0][2] == token and self.tabuleiro[1][2] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[0][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[0][2] == token):
            return True
        return False

def write_CSV_DICT(filepath, data, headers, delim = ";"):
    with open(filepath, "w", newline='') as file:
        writer = csv.DictWriter(file, delimiter=delim, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def readlista_CSV(filepath, lista, delim = ";") :
    with open(filepath, "r") as file:
        data = csv.reader(file, delimiter=delim)
        for row in data:
            lista.append(row)

def read_CSV(filepath, delim = ";") :
    with open(filepath, "r") as file:
        data = csv.reader(file, delimiter=delim)
        for row in data:
            print("\t".join(row))

def menu():
    escolha = int(input('''
    Menu
1 - Iniciar o jogo 
2 - Ver Ranking
3 - Sair do jogo
Escolha: '''))
    if escolha == 1:
        return escolha
    elif escolha == 2:
        return escolha
    elif escolha == 3:
        return escolha
    else:
        print('Escolha invalida, tente novamente')
        menu()

filePath = "ranking.csv"

#Inserir dados do jogador1
jogador1nome = input("Nome do jogador: ")
jogador1token = input("Token que o jogador1 pretende usar: ")
jogador1pontuaçao = 0
jogador1jogos = 0
jogador1 = Jogador(jogador1nome, jogador1token, jogador1pontuaçao, jogador1jogos)

#Inserir dados do jogador2
jogador2nome = input("Nome do jogador: ")
jogador2token = input("Token que o jogador2 pretende usar: ")
jogador2pontuaçao = 0
jogador2jogos = 0

while True:
    if jogador1token == jogador2token: 
        jogador2token = input("Token que o jogador2 que prente usar: ")
    else:
        jogador2 = Jogador(jogador2nome, jogador2token, jogador2pontuaçao, jogador2jogos)
        break

lista_jogador = []
readlista_CSV(filePath,lista_jogador)

escolha = menu()

while True:
    if escolha == 1:
        jogar = Tabuleiro()
        print(jogar)
        print("Jogador1 {}: {} jogador2 {}: {}".format(jogador1.nome,jogador1.token,jogador2.nome,jogador2.token))

        numero_max_jogadas = 0
        # Este ciclo serve para enquanto a 9 jogadas não forem jogadas ou não existir vencedor o programa continua a pedir jogadas aos utilizadores
        while numero_max_jogadas < 9:
            jogada = input("{}, escreva a posição que pretende jogar (A1-C3): ".format(jogador1.nome))
            if jogada == "Desistir" or jogada == "desistir":
                jogador2.pontuaçao += 3
                break
            while jogar.validar_jogada(jogada,jogador1.token) == False:
                jogada = input("{}, escreva a posição que pretende jogar (A1-C3): ".format(jogador1.nome))
                if jogar.validar_jogada(jogada,jogador1.token) == True:
                    break
            print(jogar)
            jogar.vencedor(jogador1.token)
            if jogar.vencedor(jogador1.token) == True:
                print("O vencedor é o: ",jogador1.nome)
                jogador1.pontuaçao += 3
                break
            numero_max_jogadas += 1
            if numero_max_jogadas == 9:
                break
            jogada = input("{}, escreva a posição que pretende jogar (A1-C3): ".format(jogador2.nome))
            if jogada == "Desistir" or jogada == "desistir":
                jogador1.pontuaçao += 3
                break
            while jogar.validar_jogada(jogada,jogador2.token) == False:
                jogada = input("{}, escreva a posição que pretende jogar (A1-C3): ".format(jogador2.nome))
                if jogar.validar_jogada(jogada,jogador2.token) == True:
                    break
            print(jogar)
            if jogar.vencedor(jogador2.token) == True:
                print("O vencedor é o: ",jogador2.nome)
                jogador2.pontuaçao += 3
                break
            numero_max_jogadas += 1
            
    #Se as 9 jogadas forem feitas e não exister vencedor temos empate
        if numero_max_jogadas == 9:
            print("empate")
            jogador1.pontuaçao += 1
            jogador2.pontuaçao += 1
        
        jogador1.jogos += 1
        jogador2.jogos += 1

        lista_jogador = [[jogador1.nome, jogador1.token, jogador1.pontuaçao, jogador1.jogos],
                         [jogador2.nome, jogador2.token, jogador2.pontuaçao, jogador2.jogos]]


        header = ["Nome", "Token", "Pontuação", "Jogos"]
        novaLista = [dict(zip(header, row)) for row in lista_jogador]
        write_CSV_DICT(filePath, novaLista, header)

        escolha = menu()
    elif escolha == 2:
        read_CSV(filePath)
        escolha = menu()
    elif escolha == 3:
        print('Sair do jogo ')
        break