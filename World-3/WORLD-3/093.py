dados = {'nome':'','qtd_partidas':int(),'Gols_por_Jogo':'','GolsTotal':''}
Gols_por_Jogo = []
GolTot = 0

nome = input('Digite o nome do jogador: ')
qtd_partidas = int(input('Quantas partidas foram jogadas: '))

dados['nome'] = nome
dados['qtd_partidas'] = qtd_partidas

for i in range(qtd_partidas):
    qtd_golsJogos = int((input(f'Quantos gols foi feito na {i+1}° partida: ')))

    Gols_por_Jogo.append(qtd_golsJogos)
    dados['Gols_por_Jogo'] = Gols_por_Jogo

for gol in Gols_por_Jogo:
    GolTot += gol

dados['GolsTotal'] = GolTot

print('-='*30)
print(f'Nome do jogador: {dados["nome"]}')
print(f'Gols por jogo: {dados["Gols_por_Jogo"]}')
print(f'Gols Total: {dados["GolsTotal"]}')

print('-='*30)
print(f'O jogador {dados["nome"]} jogou {dados["qtd_partidas"]} partidas.')

for partida, gols in zip(range(dados['qtd_partidas']), dados['Gols_por_Jogo']):
    print(f'=> Na partida {partida + 1}°, fez {gols} gols.')
print(f'Total de gols: {dados["GolsTotal"]}')

# Este código tem como objetivo calcular e exibir o desempenho de um jogador em várias partidas de futebol, com base
# no número de gols feitos em cada uma delas. O programa pede ao usuário o nome do jogador, o número de partidas jogadas
# e a quantidade de gols feitos em cada partida. Em seguida, o código calcula o total de gols e apresenta um resumo com
# todas as informações inseridas.


# This code aims to calculate and display a player's performance in several football matches based on the number of goals
# scored in each match. The program asks the user for the player's name, the number of matches played, and the number of
# goals scored in each match. Then, the code calculates the total goals and presents a summary with all the entered
# information