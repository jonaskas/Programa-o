"""
Jogo do Galo
"""
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
                jogada = input("Tente Outravez!\n>> ")
                self.validarjogada(jogada,token)
        else:
            print("Jogada Inválida!")
            jogada = input("Tente Outravez!\n>> ")
            self.validarjogada(jogada,token)

    def ver(self, token, nome):
        if  (self.lista[0][0] == token and self.lista[0][1] == token and self.lista[0][2] == token) or \
            (self.lista[1][0] == token and self.lista[1][1] == token and self.lista[1][2] == token) or \
            (self.lista[2][0] == token and self.lista[2][1] == token and self.lista[2][2] == token) or \
            (self.lista[0][0] == token and self.lista[1][0] == token and self.lista[2][0] == token) or \
            (self.lista[0][1] == token and self.lista[1][1] == token and self.lista[2][1] == token) or \
            (self.lista[0][2] == token and self.lista[1][2] == token and self.lista[2][2] == token) or \
            (self.lista[0][0] == token and self.lista[1][1] == token and self.lista[2][2] == token) or \
            (self.lista[2][0] == token and self.lista[1][1] == token and self.lista[0][2] == token):
          
            return False
        return True

class jogador():
    
    def __init__(self):
        self.nome = ""
        self.token = ""


    def validarjogador(self):
        while j1.token == j2.token:
            print("Token do Jogador 2 repetido!")
            j2.token = input("[Jogador 2] Introduza um novo Token: ")
        return self.token

###################
t = Tabuleiro()
j1 = jogador()
j2 = jogador()
j1.nome = "Andre"
j1.token = "X"
j2.nome = "Filipe"
j2.token = "O"
#################

for x in range (0, 9):
    print(t)
    jogada = input("{} Escolha as coordenadas\nSe quiser sair pressione a tecla 9.\n>>  ".format(j1.nome))
    if jogada == "9":
        print("O {} desistiu!! \nO venncedor é o {}. ".format(j1.nome, j2.nome))
        break
    else:
        t.validarjogada(jogada, j1.token)
        print(t)
        t.ver(j1.nome, j1.token)
    if t.ver == True:
        print("O vencedor é ", j1.nome)
        break
else:
    print("Empate")
    