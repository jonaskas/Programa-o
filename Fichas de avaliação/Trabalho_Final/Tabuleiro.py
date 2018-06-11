"""
Class Tabuleiro
"""

class Tabuleiro():

    def __init__(self):
        self.lista = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]


#Foi buscar a Internet
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


#Colocar o token na coluna e linha certa
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

