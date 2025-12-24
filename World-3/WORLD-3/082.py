valores = []
valores_par = []
valores_impares = []

while True:
    print('Digite um valor: ',end='')
    valor = int(input())
    valores.append(valor)

    if valor % 2 == 0:

        valores_par.append(valor)
    else:
        valores_impares.append(valor)
    
    print('Deseja continuar [s/n]: ',end='')
    resp = input().lower()

    if resp == 'n':
        break

print('Os valores digitados foram: {}'.format(' - '.join(map(str,valores))))

if len(valores_par) == 0:
    print('Os valores pares digitados foram: X')
else:
    print('Os valores pares digitados foram: {} '.format(' - '.join(map(str,valores_par))))

if len(valores_impares) == 0:
     print('Os valores ímpares  digitados foram: X ')
else:
    print('Os valores ímpares  digitados foram: {} '.format(' - '.join(map(str,valores_impares))))

# Este programa em Python solicita ao usuário que insira números inteiros e os armazena em três listas:
# uma para todos os valores digitados, uma para os números pares e uma para os números ímpares. O usuário
# pode continuar inserindo valores até decidir parar, digitando 'n'. Após a inserção, o programa exibe:

# 1- A lista completa de valores digitados.
# 2- A lista de valores pares ou uma mensagem indicando que nenhum valor par foi digitado.
# 3- A lista de valores ímpares ou uma mensagem indicando que nenhum valor ímpar foi digitado.


# This Python program asks the user to input integer numbers and stores them in three lists: one for all the
# entered values, one for the even numbers, and one for the odd numbers. The user can continue entering
# values until they decide to stop by typing 'n'. After the input, the program displays:

# 1- The complete list of entered values.
# 2- The list of even values or a message indicating that no even values were entered.
# 3- The list of odd values or a message indicating that no odd values were entered.