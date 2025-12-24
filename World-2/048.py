cont = 0
soma = 0
print('Digite [0] para iniciar o programa: ',end='')
start = int(input())

if start == 0:
    for impares in range(1,501,2):
       if impares % 3 == 0: 
        
          soma += impares
          cont += 1
    
    print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))

else:
    print('Erro...')

# O programa para somar números ímpares em Python foi projetado para calcular a soma
# de uma sequência de números ímpares dentro de uma faixa especificada. O usuário é
# solicitado a inserir '0' para iniciar o programa, após o qual o programa calcula a
# soma de números ímpares de 0 a 500, incrementando de 3 em 3. O resultado é exibido
# como a soma dos números ímpares na faixa especificada.
    

# The program for summing odd numbers in Python is designed to calculate the sum of a sequence
# of odd numbers within a specified range. The user is prompted to input '0' to initiate the program,
# after which the program calculates the sum of odd numbers from 0 to 10, incrementing by 3. The result
# is displayed as the sum of the odd numbers in the specified range