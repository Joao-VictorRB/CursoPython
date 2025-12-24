from random import randint
import time 

def Sorteia(num):
    print('Sorteando 5 valores da lista: ',end='')
    for i in range(0,5):
        sorteio = randint(1,5)
        num.append(sorteio)
        print(f'{sorteio} ',end='',flush=True)
        time.sleep(1)
    print('PRONTO!')
    

def SomaPar(num):
    pares = 0
    for numero in num:
        if numero % 2 == 0:
            pares += numero
    print(f'Somando os valores pares de {num}, temos {pares}')


num = []
Sorteia(num)
SomaPar(num)

# O código sorteia 5 números aleatórios entre 1 e 5, armazena-os em uma lista e, em seguida, soma apenas os números pares
#  dessa lista, exibindo tanto os números sorteados quanto o resultado da soma dos pares.


# The code generates 5 random numbers between 1 and 5, stores them in a list, and then sums only the even numbers from
# that list, displaying both the sorted numbers and the sum of the even numbers.