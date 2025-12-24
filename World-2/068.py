from random import randint

contador = 0

while True:
    print('Digite um valor: ',end='')
    num = int(input())
    print('Par ou Ímpar [P/I]: ',end='')
    resp = input().upper()

    while resp not in  'PI':
       print('Par ou Ímpar [P/I]: ',end='')
       resp = input().upper()

    computador = randint(0,10)

    print('='*30)

    soma = (num + computador) % 2

    if soma == 0 and resp == 'P':
       print('Você jogou {} e o computador {}. Total de {} DEU PAR'.format(num, computador, num + computador))
       print('Você VENCEU!!!')
       contador += 1
    
    elif soma != 0 and resp == 'I':
       print('Você jogou {} e o computador {}. Total de {} DEU ÍMPAR'.format(num, computador, num + computador))
       print('Você VENCEU!!!')
       contador += 1

    else:
       break

print('Você jogou {} e o computador {}. Total de {} DEU ÍMPAR'.format(num, computador, soma))
print('Você PERDEU!')
print('GAME OVER! Você venceu {} vezes'.format(contador))

# Este programa simula um jogo de "Par ou Ímpar" entre o usuário e o computador. O computador escolhe
# um número aleatório entre 0 e 10. Em cada rodada, o usuário insere um número e escolhe se a soma dos
# dois números será par ou ímpar. O programa então calcula a soma e verifica se a escolha do usuário 
# está correta. Se o usuário acertar, o programa incrementa um contador de vitórias e continua o jogo.
# Se o usuário errar, o jogo termina e o programa exibe o número total de vitórias do usuário.


# This program simulates a "Even or Odd" game between the user and the computer. The computer selects a
# random number between 0 and 10. In each round, the user enters a number and chooses whether the sum of
# the two numbers will be even or odd. The program then calculates the sum and checks if the user's choice
# is correct. If the user is correct, the program increments a win counter and continues the game. If the
# user is incorrect, the game ends and the program displays the total number of user wins.