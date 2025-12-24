valores = []

for c in range(1,6):
    print('Digite um valor: ',end='')
    n = int(input())

    if c == 0 or n > valores[ - 1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            
            if n <= valores[pos]:
               valores.insert(pos, n)
               break
            
            pos += 1
print('-'*30)

print('Os valores digitados em ordem foram {}'.format(valores))

# Este programa em Python solicita ao usuário que insira 5 números inteiros e os armazena em uma
# lista de forma ordenada. Ele garante que os números sejam inseridos na lista já em ordem crescente,
# independentemente da ordem de entrada do usuário. Após inserir todos os valores, o programa exibe a
# lista com os números ordenados.


# This Python program asks the user to input 5 integer numbers and stores them in a list in an ordered manner.
# It ensures that the numbers are inserted into the list in ascending order, regardless of the order in which
# the user enters them. After all values are entered, the program displays the list with the numbers sorted.