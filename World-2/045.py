import random
import time

computador = random.randint(1,3)

print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')

print('Qual é a sua jogada: ',end='')
menu = int(input())

time.sleep(.8)
print('JO')
time.sleep(.8)
print('KEN')
time.sleep(.8)
print('PÔ!!!')

if menu == computador and menu == 1 and computador == 1:
    print('Jogador: PEDRA')
    print('Computador: PEDRA')
    print('\033[1;33mEMPATE\033[m')
    
elif menu == 2 and computador == 2:
    print('Jogador: PAPEL')
    print('Computador: PAPEL')
    print('\033[1;33mEMPATE\033[m')
   
elif menu == 3 and computador == 3:
    print('Jogador: TESOURA')
    print('Computador: TESOURA')
    print('\033[1;33mEMPATE\033[m')

elif menu == 1 and computador == 2:
    print('Jogador: REDRA')
    print('Computador: PAPEL')
    print('\033[1;31mPERDEU\033[m')

elif menu == 2 and computador == 1:
    print('Jogador: PAPEL')
    print('Computador: PEDRA')
    print('\033[1;32mVENCEU\033[m')

elif menu == 1 and computador == 3:
    print('Jogador: PAPEL')
    print('Computador: TESOURA')
    print('\033[1;32mVENCEU\033[m')
elif menu == 3 and computador == 1:
    print('Jogador: TESOURA')
    print('Computador: PEDRA')
    print('\033[1;31mPERDEU\033[m')

elif menu == 2 and computador == 3:
    print('Jogador: PAPEL')
    print('Computador: TESOURA')
    print('\033[1;31mPERDEU\033[m')
elif menu == 3 and computador == 2:
    print('Jogador: TESOURA')
    print('Computador: PAPEL')
    print('\033[1;32mVENCEU\033[m')

else:
    print('Erro...')

# O Programa de Jokenpô em Python é uma aplicação desenvolvida para simular
# o clássico jogo de "Pedra, Papel e Tesoura". Este programa interativo permite
# que os usuários joguem contra o computador em uma competição de escolhas entre
# as três opções disponíveis: Pedra, Papel e Tesoura.
    

# The Rock, Paper, Scissors Game Program in Python is an application developed to
# simulate the classic game of "Rock, Paper, Scissors." This interactive program
# allows users to play against the computer in a competition of choices among the
# three available options: Rock, Paper, and Scissors.