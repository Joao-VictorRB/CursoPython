from random import randint

lista = []
jogos = []
print('--------------JOGO DA MEGA SENA ------------------')
quant = int(input(' Quantos jogos você quer:'))

tot = 1

while tot <= quant:
    cont = 0
    while True:

        num = randint(1,60)

        if num not in lista:
            lista.append(num)
            cont += 1
        
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1 

print('-='*6, 'JOGOS', '-='*6)

for i , l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')

# Este programa gera jogos da Mega Sena de forma aleatória. O usuário pode escolher quantos jogos deseja e,
# em seguida, o programa cria esses jogos, cada um com 6 números únicos e aleatórios entre 1 e 60. Para garantir
# que não haja números repetidos dentro de um mesmo jogo, o programa verifica se o número gerado já foi sorteado
# antes de adicioná-lo à lista. Após gerar todos os jogos solicitados, o programa exibe uma lista com os números
# de cada jogo gerado. A saída é organizada e apresenta o número de cada jogo gerado.


# This program generates random Mega Sena lottery games. The user can choose how many games they want, and the
# program will then create those games, each consisting of 6 unique random numbers between 1 and 60. To ensure
# that there are no duplicate numbers within the same game, the program checks if the generated number has already
# been drawn before adding it to the list. After generating all the requested games, the program displays a list
# with the numbers for each generated game. The output is organized and shows the number of each generated game.        