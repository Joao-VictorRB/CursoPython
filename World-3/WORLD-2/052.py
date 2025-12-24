print('Digite um número inteiro:',end='')
n = int(input())

for c in range(0,3):

    d1 = n/1
    d2 = n%2
    d3 = n/n

if d1 == n and d2 != 0 and d3 == 1:

    print('O número {} É primo'.format(n))
else:
    print('O número {} NÃO é primo'.format(n))

# Este programa em Python solicita ao usuário que insira um número inteiro.
# Em seguida, utiliza um loop para calcular três variáveis, representando
# divisões do número de diferentes formas. Depois de realizar esses cálculos,
# o programa verifica se o número atende a certas condições para ser considerado primo.
# Se atender, imprime que o número é primo; caso contrário, imprime que não é primo. 


# This Python program prompts the user to input an integer. Then, it uses a loop to calculate
# three variables representing divisions of the number in different ways. After these calculations,
# the program checks if the number meets certain conditions to be considered prime. If it does, it
# prints that the number is prime; otherwise, it prints that it is not prime.