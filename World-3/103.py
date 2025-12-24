def Ficha(nome = '<Desconhecido>', gols = 0):
    print(f'O jogador: {nome} fez {gols} gols(s).')
    
        
nome = input('Qual o nome do jogador: ').strip().capitalize()
gols_input = input('Digite a quantidade de gols: ').strip()

if gols_input.isnumeric():
    gols_input = int(gols_input)
else:
    gols_input = 0

if nome.strip() == '':
    Ficha(gols = gols_input)
else:
    Ficha(nome, gols_input)

# A função Ficha(nome = '<Desconhecido>', gols = 0) exibe uma mensagem informando o nome do jogador e a quantidade de gols
# feitos por ele. Os parâmetros nome e gols têm valores padrão, sendo '<Desconhecido>' para o nome e 0 para a quantidade de
# gols. O código solicita ao usuário o nome do jogador e o número de gols, fazendo algumas verificações. Se o nome estiver
# vazio, o valor padrão é utilizado. Para os gols, o código verifica se a entrada é um número válido, e se não for, assume
# que o jogador fez 0 gols. Dependendo das entradas, a função Ficha é chamada com os valores fornecidos ou os valores padrão.
    

# The function Ficha(nome = '<Desconhecido>', gols = 0) displays a message with the player's name and the number of goals 
# they scored. The parameters nome and gols have default values: '<Desconhecido>' for the name and 0 for the goals. The 
# code prompts the user for the player's name and the number of goals, performing some checks. If the name is left empty, 
# the default value is used. For the goals, the code checks if the input is a valid number, and if not, assumes the player
# scored 0 goals. Based on the inputs, the Ficha function is called with the provided or default values.