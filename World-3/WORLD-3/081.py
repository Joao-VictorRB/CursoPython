valores = []

while True:
    
    print('Digite um valor: ',end='')
    v = int(input())

    valores.append(v)
    print('-'*40)
    print('Deseja registrar outro valor [s/n]: ',end='')
    resposta = input().lower()

    if resposta in 'n':
        break

print('Quantidade de valores digitados: {}'.format(len(valores)))
valores_revertidos = list(reversed(sorted(valores)))
print('Lista na forma descrescente: {}'.format(" > ".join(map(str, valores_revertidos))))

if 5 in valores:
    print('A lista contém o valor 5 na posição: {}'.format(valores.index(5)))
else:
    print('A lista não contém o valor 5')

# Este programa solicita ao usuário que insira valores inteiros repetidamente, os armazena em uma lista e permite
# que o usuário adicione mais valores até que decida parar, digitando 'n'. Após o término da inserção, o programa
# exibe a quantidade de valores digitados e a lista ordenada de forma decrescente, com os valores separados por
# " > ". Além disso, verifica se o número 5 está na lista e, caso esteja, mostra sua posição. Se o número 5 não
# estiver na lista, o programa informa isso ao usuário.


# This program repeatedly asks the user to input integer values, stores them in a list, and allows the user to add
# more values until they decide to stop by typing 'n'. After the input process is finished, the program displays
# the number of values entered and the list sorted in descending order, with values separated by " > ". Additionally,
# it checks if the number 5 is in the list and, if it is, shows its position. If the number 5 is not in the list,
# the program informs the user about it.