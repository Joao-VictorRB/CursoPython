print('Digite o número da tabuada: ',end='')
n = int(input())
contador = 1
print(4*('-=-'))
for tabuada in range (1,11):
    print('{} X {} = {}'.format(n,contador, n*contador))
    contador = contador + 1
print(4*('-=-'))

#O Programa de Tabuada em Python foi projetado para gerar e exibir a tabuada de um
#número inserido pelo usuário. O programa solicita que o usuário insira o número desejado
#para o qual a tabuada será calculada. A tabuada é então exibida, mostrando a multiplicação
#do número escolhido pelos inteiros de 1 a 10.


#The Multiplication Table Program in Python is designed to generate and display the multiplication
#table for a user-inputted number. The program prompts the user to input the desired number for which
#the multiplication table will be calculated. The multiplication table is then displayed, showcasing
#the multiplication of the chosen number by integers from 1 to 10