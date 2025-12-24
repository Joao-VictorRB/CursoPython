while True:
    print('Quer ver a tabuada de qual valor: ',end='')
    v = int(input())

    if v < 0:
        break

    for c in range(1,11):
        print('{} X {} = {}'.format(v,c, v * c))

print('Tabuada finalizada!')

# Este programa exibe a tabuada de multiplicação para um número fornecido pelo usuário. O usuário é
# solicitado a inserir um número, e o programa exibe a tabuada de 1 a 10 para esse número. Se o usuário
# inserir um número negativo, o programa termina. O ciclo é repetido até que um número negativo seja
# inserido, momento em que o programa exibe uma mensagem indicando que a tabuada foi finalizada.


# This program displays the multiplication table for a number provided by the user. The user is prompted
# to enter a number, and the program displays the multiplication table from 1 to 10 for that number.
# If the user enters a negative number, the program terminates. The cycle repeats until a negative number
# is entered, at which point the program displays a message indicating that the multiplication table has
# been finalized.