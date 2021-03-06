"""
Jogo do Galo
"""


class Tabuleiro():
    def __init__(self):
        self.lista = [[None, None, None],
                       [None, None, None], 
                       [None, None, None]]
        

    def __str__(self): #Foi buscar a Internet
        stroutput = "  |A|B|C|"
        for i in range(0, 3):
            stroutput += "\n" + str(i+1) + "|"
            for j in range(0, 3):
                if self.lista[i][j] == None:
                    stroutput += " |"
                else:
                    stroutput += self.lista[i][j] + "|"
        return stroutput

#Colocar o token na coluna e linha certa
    def validarjogada(self, jogada, token):        
        if (jogada[0] == "A" or jogada[0] == "B" or jogada[0] == "C" or jogada[0] == "a" or jogada[0] == "b" or jogada[0] == "c" ) and (jogada[1] == "1" or jogada[1] == "2" or jogada[1] == "3"):
            if jogada[0] == "A":
                coluna = 0
                linha = int(jogada [1]) - 1
                if self.lista[linha][coluna] == None:
                    self.lista[linha][coluna] = token
                else:
                    print("Jogada invalida!!")
                    jogada = input("Tente outravez!\n>> ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "B":
                coluna = 1
                linha = int(jogada [1]) - 1
                if self.lista[linha][coluna] == None:
                    self.lista[linha][coluna] = token
                else:
                    print("Jogada invalida!!")
                    jogada = input("Tente outravez!\n>> ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "C": 
                coluna = 2
                linha = int(jogada [1]) - 1
                if self.lista[linha][coluna] == None:
                    self.lista[linha][coluna] = token
                else:
                    print("Jogada invalida!!")
                    jogada = input("Tente outravez!\n>> ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "a":
                coluna = 0
                linha = int(jogada [1]) - 1
                if self.lista[linha][coluna] == None:
                    self.lista[linha][coluna] = token
                else:
                    print("Jogada invalida!!")
                    jogada = input("Tente outravez!\n>> ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "b":
                coluna = 1
                linha = int(jogada [1]) - 1
                if self.lista[linha][coluna] == None:
                    self.lista[linha][coluna] = token
                else:
                    print("Jogada invalida!!")
                    jogada = input("Tente outravez!\n>> ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "c": 
                coluna = 2
                linha = int(jogada [1]) - 1
                if self.lista[linha][coluna] == None:
                    self.lista[linha][coluna] = token
                else:
                    print("Jogada invalida!!")
                    jogada = input("Tente outravez!\n>> ")
                    self.validarjogada(jogada,token)
        else:
            print("Jogada invalida!!")
            jogada = input("Tente outravez!\n>> ")
            self.validarjogada(jogada,token)

          
    def ver(self, token, nome):
        if(self.lista[0][0] == token and self.lista[0][1] == token and self.lista[0][2] == token) or \
          (self.lista[1][0] == token and self.lista[1][1] == token and self.lista[1][2] == token) or \
          (self.lista[2][0] == token and self.lista[2][1] == token and self.lista[2][2] == token) or \
          (self.lista[0][0] == token and self.lista[1][0] == token and self.lista[2][0] == token) or \
          (self.lista[0][1] == token and self.lista[1][1] == token and self.lista[1][2] == token) or \
          (self.lista[0][2] == token and self.lista[1][2] == token and self.lista[2][2] == token) or \
          (self.lista[0][0] == token and self.lista[1][1] == token and self.lista[2][2] == token) or \
          (self.lista[2][0] == token and self.lista[1][1] == token and self.lista[0][2] == token):
            global winner
            print("Vencedor")
            winner = True
        return winner

###############################################

#Defenir o nome e o token do jogador
class jogador():
    
    def __init__(self):
        self.nome = ""
        self.token = ""


    def validarjogador(self):
        while j1.token == j2.token:
            print("Token do Jogador 2 repetido!")
            j2.token = input("[Jogador 2] Introduza um novo Token: ")
        return self.token

###############################################

#Introducao dos dados
j1 = jogador()
j1.nome = input('Introduza o seu nome: ')
j1.token = input('Introduza um token: ')

j2 = jogador()
j2.nome = input('Introduza o seu nome: ')
j2.token = input('Introduza um token: ')


t = Tabuleiro()
j1.validarjogador()
t.__str__()
num_max_jogadas = 0

##############################################
#Jogar
vencedor = False
while num_max_jogadas < 9:
    print(t)
    jogada = input("{} Escolha as coordenadas! (COM MAIUSCULAS)\n Se quiser desistir pressione a tecla 9.\n>>  ".format(j1.nome))
    if jogada == 9:
        print("O {} desistiu! \n O vencedor é o {}.  ".format(j1.nome,j2.nome))
        break
    t.validarjogada(jogada,j1.token)
    print(t)
    t.ver(j1.nome, j1.token)
    if vencedor == True:
        print("O vencedor é ",j1.nome)
        break
    num_max_jogadas += 1
    if num_max_jogadas == 9:
        print("Empate")
        break
    jogada = input("{} Escolha as coordenadas! (COM MAIUSCULAS)\n Se quiser desitir pressione a tecla 9.\n>>  ".format(j2.nome))
    if jogada == 9:
        print("O {} desistiu! \n O vencedor é o {}.  ".format(j1.nome,j2.nome))
        break
    t.validarjogada(jogada,j2.token)
    print(t)
    t.ver(j2.nome, j2.token)
    if vencedor == True:
        print("O vencedor é ",j2.nome)
        break
num_max_jogadas += 1