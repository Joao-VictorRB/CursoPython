from random import randint
from time import sleep

jogadores = {'player_1':randint(1,6),'player_2':randint(1,6),'player_3':randint(1,6),'player_4':randint(1,6)}

for k,v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print()

ranking = {k: v for k, v in sorted(jogadores.items(), key=lambda item: item[1], reverse = True)}
lugar = 1

print('Ranking dos jogadores:')
print()
for  k, v  in ranking.items():
    
    print(f'{lugar}° lugar: {k} com {v}')
    lugar += 1
    sleep(1)

# O código simula o lançamento de dados para 4 jogadores e organiza um ranking com base nos valores obtidos. Para cada
# jogador, o programa sorteia um número entre 1 e 6 e armazena o resultado. Após o preenchimento dos resultados de
# todos os jogadores, o programa ordena os jogadores em ordem decrescente com base nos números sorteados e exibe o
# ranking final, indicando o lugar de cada jogador e seu respectivo valor.


#The code simulates a dice roll for 4 players and organizes a ranking based on the values obtained. For each player,
# the program rolls a number between 1 and 6 and stores the result. After all players have their results, the program
# sorts them in descending order based on the rolled numbers and displays the final ranking, showing each player's
# position and the value they rolled.