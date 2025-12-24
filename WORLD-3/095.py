DadosJogadores = []
registro = {'nome':'','qtd_partidas':int(),'Gols_por_Jogo':'','GolsTotal':''}
Gols_por_Jogo = []
GolTot = 0

while True:
    nome = input('Digite o nome do jogador: ')
    qtd_partidas = int(input('Quantas partidas foram jogadas: '))

    registro['nome'] = nome
    registro['qtd_partidas'] = qtd_partidas

    for i in range(qtd_partidas):
        qtd_golsJogos = int((input(f'Quantos gols foi feito na {i+1}° partida: ')))

        Gols_por_Jogo.append(qtd_golsJogos)
        registro['Gols_por_Jogo'] = Gols_por_Jogo

    for gol in Gols_por_Jogo:

        GolTot += gol

    registro['GolsTotal'] = GolTot

    DadosJogadores.append(registro.copy())

    Gols_por_Jogo = []
    GolTot = 0
    registro['nome'] = ''
    registro['qtd_partidas'] = 0
    registro['Gols_por_Jogo'] = ''
    registro['GolsTotal'] = 0

    resp = (input('Deseja continuar (S/N): ')).upper()

    if resp in 'N':
        break

print(f'{"Cod":<5} {"Nome":<20} {"Gols":<20} {"Total":<10}')

for i, k in enumerate(DadosJogadores):
   
    print(f'{i:<5} {str(k["nome"]):<20} {str(k["Gols_por_Jogo"]):<20} {str(k["GolsTotal"]):<10}')

while True:
    print('-' * 40)
    resp = int(input('Mostrar dados de qual jogador? (999 interrompe): '))

    if resp == 999:
        break
    
    if resp >= 0 and resp < len(DadosJogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {DadosJogadores[resp]["nome"]}:')
    else:
        print('Jogador não existete na lista!!!')
           
    for partida, gols in zip(range(DadosJogadores[resp]['qtd_partidas']), DadosJogadores[resp]['Gols_por_Jogo']):
        print(f'=> Na partida {partida + 1}°, fez {gols} gols.')
    print(f'=> Total de gols: {DadosJogadores[resp]["GolsTotal"]}')

print('PROGRAMA ENCERRADO!!')

# Este código tem como objetivo realizar o cadastro de vários jogadores de futebol, armazenando o nome, quantidade de
# partidas jogadas, os gols feitos por jogo e o total de gols de cada jogador. O programa permite que o usuário cadastre
# múltiplos jogadores, insira os dados de partidas e gols, e, em seguida, armazene essas informações em uma lista de
# dicionários. Após o cadastro, o programa exibe uma tabela organizada com os dados dos jogadores e permite consultar
# as informações detalhadas de cada jogador.


# This code aims to register several football players, storing the player's name, the number of matches played, the goals
# scored in each game, and the total goals scored by each player. The program allows the user to register multiple
# players, enter match and goal data, and then store this information in a list of dictionaries. After registration,
# the program displays a well-organized table with the players' data and allows querying detailed information for each
# player.