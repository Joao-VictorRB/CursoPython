import time

print('Digite [0] para iniciar o programa: ',end='')
start = int(input())

if start == 0:
    time.sleep(2)
    for pares in range(2,51, 2):
        print(pares, end=' ')
else: 
    print('Erro...')

# O programa para exibir números pares em Python foi projetado para apresentar uma
# sequência de números pares dentro de uma faixa especificada. O programa solicita que
# o usuário insira '0' para iniciar o programa, introduzindo um  atraso de dois segundos
# antes de exibir números pares de 0 a 50 em incrementos de 2. O módulo 'time' é utilizado
# para incorporar o atraso, aprimorando a experiência geral do usuário.
    

# The program for displaying even numbers in Python is designed to showcase a sequence of even numbers
# within a specified range. The program prompts the user to input '0' to initiate the program, introducing
# a two-second delay before displaying even numbers from 0 to 50 in increments of 2. The 'time' module is 
# utilized to incorporate the delay, enhancing the overall user experience