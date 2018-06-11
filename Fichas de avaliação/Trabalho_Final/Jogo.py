from Jogador import jogador
from Tabuleiro import Tabuleiro
from listas import write_CSV_DICT,readlista_CSV,read_CSV


#Esta função serve para mostrar um menu
def menu():
    resposta = int(input("\n\nMenu\n1-Novo Jogo\n2-Ver Ranking\n3-Sair do Jogo\n\nEscolha\n>>"))

    if resposta == 1:
        return resposta
    elif resposta == 2:
        return resposta
    elif resposta == 3:
        return resposta
    else:
        print("Escolha Invalida!\nTente Outravez!")
        menu()


########################################################################################



filePath = "Fichas de avaliação/Tabalho_Final/dados.csv"

#Introduzir o Jogador1
j1 = jogador()
print("\nJogador 1")
j1.nome = input('Introduza o seu nome: ')
j1.token = input('Introduza um token: ')
j1.pontuacao = 0
j1.jogos = 0



#Introduzir o Jogador2
j2 = jogador()
print("\nJogador 2")
j2.nome = input('Introduza o seu nome: ')
j2.token = input('Introduza um token: ')
j2.pontuacao = 0
j2.jogos = 0

while True:
    if j1.token == j2.token:
        j2.token = input('Introduza um token: ')
    else:
        break

lista_jogador = []
#readlista_CSV(filePath, lista_jogador) Não consegui por a dar esta linha


resposta = menu()
#Jogar
while True:
    if resposta == 1:
        t = Tabuleiro()
        print(t)
        numero_max_jogadas = 0
        while numero_max_jogadas < 9:
            jogada = input("Escolha as coordenadas!\nSe quiser sair pressione a tecla 9.\n{}>>  ".format(j1.nome))
            
            if jogada == "9":
                print("O {} desistiu!! \nO venncedor é o/a {}. ".format(j1.nome, j2.nome))
                j2.pontuacao += 3
                break
            t.validarjogada(jogada,j1.token)
            print(t)
            if t.ver(j1.token) == True:
                print("O vencedor é o/a", j1.nome)
                j1.pontuacao += 3
                break

            numero_max_jogadas +=1
            if numero_max_jogadas == 9:
                break

            jogada = input("Escolha as coordenadas!\nSe quiser sair pressione a tecla 9.\n{}>>  ".format(j2.nome))
            if jogada == "9":
                print("O {} desistiu!! \nO venncedor é o/a {}. ".format(j2.nome, j1.nome))
                j1.pontuacao += 3
                break
            t.validarjogada(jogada,j2.token)
            print(t)
            if t.ver(j2.token) == True:
                print("O vencedor é o/a", j2.nome)
                j2.pontuacao += 3
                break
            numero_max_jogadas += 1

        if numero_max_jogadas == 9:
            print("Empate")
            j1.pontuacao +=1
            j2.pontuacao +=1
            break
        
        j1.jogos += 1
        j2.jogos += 1

        lista_jogador = [[j1.nome, j1.token, j1.pontuacao, j1.jogos],
                        [j2.nome, j2.token, j2.pontuacao, j2.jogos]]


        header = ["Nome", "Token", "Pontuação", "Jogos"]
        novaLista = [dict(zip(header, row)) for row in lista_jogador]
        #write_CSV_DICT(filePath, novaLista, header) Não consegui por a dar esta linha


        resposta = menu()
    elif resposta == 2:
        #read_CSV(filePath) Não consegui por a dar esta linha
        resposta = menu()
    elif resposta == 3:
        print('Sair do jogo')
        break