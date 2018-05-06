
import random


class Tabuleiro():
    def __init__(self):
        self.A = [None, None, None]
        self.B = [None, None, None]
        self.C = [None, None, None]
        self.lista = [self.A, self.B, self.C]
        

    def devolvernumero(self, jogada1): 
        if jogada1 == "A":
            return 0
        elif jogada1 == "B":
            return 1
        elif jogada1 == "C":
            return 2 

    def completar(self, jogada1, jogada2, token): 
        v = self.devolvernumero(jogada1)
        if (self.lista[jogada2][v]) == None:
            self.lista[jogada2][v] = token
            return True
        else:
            return False

    def __str__(self): #Mostrar o tabuleiro
        stroutput = "  A|B|C|"
        for i in range(0, 3):
            stroutput += "\n" + str(i+1) + "|"
            for j in range(0, 3):
                if self.lista[i][j] == None:
                    stroutput += " |"
                else:
                    stroutput += self.lista[i][j] + "|"
        return stroutput

    def ver(self, token):
        if  (self.lista[0][1] == token and self.lista[0][2] == token and self.lista[0][3] == token) or \
            (self.lista[1][1] == token and self.lista[1][2] == token and self.lista[1][3] == token) or \
            (self.lista[2][1] == token and self.lista[2][2] == token and self.lista[2][3] == token) or \
            (self.lista[0][1] == token and self.lista[2][1] == token and self.lista[3][1] == token) or \
            (self.lista[0][2] == token and self.lista[2][2] == token and self.lista[3][2] == token) or \
            (self.lista[0][3] == token and self.lista[2][3] == token and self.lista[3][3] == token) or \
            (self.lista[0][1] == token and self.lista[2][2] == token and self.lista[3][3] == token) or \
            (self.lista[0][3] == token and self.lista[2][2] == token and self.lista[3][1] == token):
            global play
            print("Vencedor")
            play = False

    def escolha_coluna(self, jogada1):
        coluna = input("Escolha a coluna onde queres jogar!\n>")
        while coluna != "a" or coluna != "b" or coluna != "c" or coluna != "A" or coluna != "B" or coluna != "C" :
            print("Coluna invalida!\nEscolha uma das colunas (A,B,C)\n")
            coluna = input("Escolha a coluna onde queres jogar!\n>")
        else: 
           return jogada1 == coluna 
        
    
    def escolha_linha(self, jogada2):
        linha = input("Escolha a linha onde queres jogar!\n>")
        while linha != 1 or linha != 2 or linha != 3 :
            print("Linha invalida!\nEscolha uma das linhas (1,2,3)\n")
            linha = input("Escolha a linha onde queres jogar!\n>")
        else: 
           return jogada2 == linha 
    
t = Tabuleiro()
play = True
token = "x"
print "%s" % (t.escolha_coluna())
t.escolha_linha()          
jogada1 = str(jogada1)
jogada2 = int(jogada2)
final = Tabuleiro()
print(final)
final.completar(jogada1, jogada2, token)
print(final)

"""

    def __str__(self):
        print(' |A |B |C |')
        print('1|{} |{} |{} |'.format(self.lista[0][0], self.lista[0][1], self.lista[0][2]))
        print('2|{} |{} |{} |'.format(self.lista[1][0], self.lista[1][1], self.lista[1][2]))
        print('3|{} |{} |{} |'.format(self.lista[2][0], self.lista[2][1], self.lista[2][2]))
"""