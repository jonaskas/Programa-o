##Variaveis globais
jogador_valido = False
num_max_jogadas = 0

##Class Jogador
class jogador():
    
    def __init__(self):
        self.nome = ""
        self.token = ""

    def validarjogador(self):
        while jogador1.token == jogador2.token:
            print("Token do Jogador 2 repetido!")
            jogador2.token = input("[Jogador 2] Introduza um novo Token: ")
        return self.token
        
##Class Tabuleiro
class tabuleiro():
    
    def __init__(self):

        self.tabuleiro = [ [None, None, None], 
                           [None, None, None], 
                           [None, None, None] ]

    def __str__(self):
        teste = "\n  A|B|C"
        for j in range (0, 3):
            teste += "\n" + str(j+1) + "|"
            for i in range (0, 3):
                if self.tabuleiro[j][i] == None:
                    teste += " |"
                else:
                    teste += self.tabuleiro[j][i] + "|"
        return teste
    
    def validarjogada(self,jogada,token):        
        if (jogada[0] == "A" or jogada[0] == "B" or jogada[0] == "C") and (jogada[1] == "1" or jogada[1] == "2" or jogada[1] == "3"):
            if jogada[0] == "A":
                coluna = 0
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == None:
                    self.tabuleiro[linha][coluna] = token
                else:
                    print("Jogada Inválida!!")
                    jogada = input("Jogue entre (A1-C3): ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "B":
                coluna = 1
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == None:
                    self.tabuleiro[linha][coluna] = token
                else:
                    print("Jogada Inválida!!")
                    jogada = input("Jogue entre (A1-C3): ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "C":
                coluna = 2
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == None:
                    self.tabuleiro[linha][coluna] = token
                else:
                    print("Jogada Inválida!!")
                    jogada = input("Jogue entre (A1-C3):")
                    self.validarjogada(jogada,token)
        else:
            print("Jogada Inválida!!")
            jogada = input("Jogue entre (A1-C3):  ")
            self.validarjogada(jogada,token)

    def vitoria(self,nome,token):
        if  (self.tabuleiro[0][0] == token and self.tabuleiro[0][1] == token and self.tabuleiro[0][2] == token) or \
            (self.tabuleiro[1][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[1][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[2][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[0][0] == token and self.tabuleiro[1][0] == token and self.tabuleiro[2][0] == token) or \
            (self.tabuleiro[1][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[1][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[2][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[0][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[0][2] == token):
            global winner
            winner = True
        return winner
    
##Introducao de dados
##Jogador 1
jogador1 = jogador()
jogador1.nome = input("[Jogador 1] Nome do jogador: ")
jogador1.token = input("[Jogador 1] Token que prente usar: ")
##Jogador 2
jogador2 = jogador()
jogador2.nome = input("[Jogador 2] Nome do jogador: ")
jogador2.token = input("[Jogador 2] Token que prente usar: ")

##Tabuleiro
tabuleiro1 = tabuleiro()
jogador1.validarjogador()    
tabuleiro1.__str__()

#Jogar
winner = False
while num_max_jogadas < 9:
    print(tabuleiro1)
    jogada = input("[{}] Onde pretende jogar:\n Se pretender desistir clique X:   ".format(jogador1.nome))
    if jogada == "X":
        print("O jogador {} desistiu \n O jogador {} é o vencedor ".format(jogador1.nome,jogador2.nome))
        break
        
    tabuleiro1.validarjogada(jogada,jogador1.token)
    print(tabuleiro1)
    tabuleiro1.vitoria(jogador1.nome,jogador1.token)
    if winner == True:
        print("O vencedor é ",jogador1.nome)
        break
    num_max_jogadas += 1
    if num_max_jogadas == 9:
        print("Empate")
        break
    jogada = input("[{}] Onde pretende jogar: ".format(jogador2.nome))
    if jogada == "X":
        print("O jogador {} desistiu \n O jogador {} é o vencedor ".format(jogador2.nome,jogador1.nome))
        break
    tabuleiro1.validarjogada(jogada,jogador2.token)
    print(tabuleiro1)
    tabuleiro1.vitoria(jogador2.nome,jogador2.token)
    if winner == True:
        print("O vencedor é ",jogador2.nome)
        break
num_max_jogadas += 1