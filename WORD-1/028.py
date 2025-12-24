from random import randint

computador = randint(0,5)

print('O computador pensou em um número entre 0 a 5, tente adivinhar: ',end='')
r=int(input())

if computador == r:
    print('Parabéns, você acertou!!!')
else:
    print('Você errou, eu pensei no {}'.format(computador))
    