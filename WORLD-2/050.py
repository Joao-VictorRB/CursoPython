lista = 0
cont = 0

for perguntas in range(1,7):
    print('Digite um valor inteiro: ',end='')
    valor = int(input())

    if valor%2 == 0:
        
       lista += valor
       cont += 1

print('Você informou {} números e soma de todos os números pares são: {}'.format(cont,lista))
    
# O programa para somar números pares em Python foi projetado para calcular a soma
# de números inteiros pares inseridos pelo usuário. O programa solicita que o usuário
# insira seis valores inteiros e verifica cada valor para determinar se é par. Se um
# valor for par, ele é adicionado a um total acumulado. Por fim, o programa exibe a
# soma de todos os números pares inseridos.


# The program for summing even numbers in Python is designed to calculate the sum of even
# integers entered by the user. The program prompts the user to input six integer values and
# checks each value for evenness. If a value is even, it is added to a running total. Finally,
# the program displays the sum of all the entered even numbers.