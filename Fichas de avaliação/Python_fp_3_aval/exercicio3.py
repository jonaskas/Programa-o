"""
Exercicio 3
"""

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
voto_em_branco = 0
voto_nulo = 0

#-------------------------Menu de escolha-----------------------------

print('\n********************************')
print('*      1-José Ribeiro          *')
print('*      2-João Gonçalves        *')
print('*      3-Maria Silva           *')
print('*      4-Nuno Ribeiro          *')
print('*                              *')
print('*      0-Voto em branco        *')
print('*      9-Voto nulo             *')
print('*     -1-Terminar a contagem   *')
print('********************************\n')

voto = int(input('Escolhe quem queres votar: '))

while voto != -1:
    if voto == 1:
        candidato1 += 1
    if voto == 2:
        candidato2 += 1
    if voto == 3:
        candidato3 += 1
    if voto == 4:
        candidato4 += 1
    if voto == 0:
        voto_em_branco += 1
    if voto == 9:
        voto_nulo += 1
    voto = int(input('Escolhe quem queres votar: '))

#---------------------------------------------------------------------

#----------------------------Calculos---------------------------------

total_de_votos = candidato1 + candidato2 + candidato3 + candidato4 + voto_em_branco + voto_nulo
percentagem_candidato1 = (candidato1 * 100) / total_de_votos
percentagem_candidato2 = (candidato2 * 100) / total_de_votos
percentagem_candidato3 = (candidato3 * 100) / total_de_votos
percentagem_candidato4 = (candidato4 * 100) / total_de_votos
percentagem_voto_em_branco = (voto_em_branco * 100) / total_de_votos
percentagem_voto_nulo = (voto_nulo * 100) / total_de_votos
#---------------------------------------------------------------------

print('\n\nO número total de votos é: {}\n'.format(total_de_votos))
print('O José Ribeiro teve uma percentagem de votos de {}%({} votos).'.format(percentagem_candidato1,candidato1))
print('O João Gonçalves teve uma percentagem de votos de {}%({} votos).'.format(percentagem_candidato2,candidato2))
print('A Maria Silva teve uma percentagem de votos de {}%({} votos).'.format(percentagem_candidato3,candidato3))
print('O Nuno Ribeiro teve uma percentagem de votos de {}%({} votos).\n'.format(percentagem_candidato4,candidato4))
print('A percentagem de votos em branco é de {}%({} votos).'.format(percentagem_voto_em_branco,voto_em_branco))
print('A percentagem de votos em branco é de {}%({} votos).'.format(percentagem_voto_nulo,voto_nulo))

