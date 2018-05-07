
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
            self.lista[jogada2][v] += token
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

    def escolha_coluna(self):
        coluna = input("Escolha a coluna onde queres jogar!\n>")
        if coluna != "a" and coluna != "b" and coluna != "c" and coluna != "A" and coluna != "B" and coluna != "C" :
            print(coluna)
            print("Coluna invalida!\nEscolha uma das colunas (A,B,C)\n")
            coluna = input("Escolha a coluna onde queres jogar!\n>")
        else: 
           return jogada1 == coluna 
        
    
    def escolha_linha(self):
        linha = input("Escolha a linha onde queres jogar!\n>")
        if linha < 0 and linha > 3 :
            print(linha)
            print("Linha invalida!\nEscolha uma das linhas (1,2,3)\n")
            linha = input("Escolha a linha onde queres jogar!\n>")
        else: 
           return jogada2 == linha 

class jogador():

    def escolhatoken(self):
        #Os jogadores escolhem os seus nomes e tokens
        nome1 = input("Jogador 1 escolha o nome que deseja utilizar: ")
        token1 = input("Jogador 1 escolha o seu token: ")
        nome2 = input("Jogador 2 escolha o nome que deseja utilizar: ")
        token2 = input("Jogador 2 escolha o seu token: ")
        while token2 == token1:
            print("O seu token e igual ao do jogador 1.")
            token2 = input(print("Jogador 2 escolha o seu token: "))
        else:
            pass

play = True 
t = Tabuleiro()
j = jogador()
final = t.__str__()
nume_max_jogadas = 0

j.escolhatoken()  
print(final)
t.escolha_coluna()
t.escolha_linha()
jogada1 = str(jogada1)
jogada2 = int(jogada2)    
while nume_max_jogadas <= 9:
         
 
    nume_max_jogadas += 1
print(final)



"""

    def __str__(self):
        print(' |A |B |C |')
        print('1|{} |{} |{} |'.format(self.lista[0][0], self.lista[0][1], self.lista[0][2]))
        print('2|{} |{} |{} |'.format(self.lista[1][0], self.lista[1][1], self.lista[1][2]))
        print('3|{} |{} |{} |'.format(self.lista[2][0], self.lista[2][1], self.lista[2][2]))
"""