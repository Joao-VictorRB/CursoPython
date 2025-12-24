print('Digite o número que você quer saber o fatorial: ',end='')
n = int(input())

fatorial = n
contador = n

while contador != 1:

   contador = contador - 1
   fatorial = fatorial * contador

print('O fatorial de {}! é = {}'.format(n,fatorial))

#Este programa Python calcula o fatorial de um número fornecido pelo usuário. Ele
#solicita ao usuário que insira o número desejado e, em seguida, utiliza um loop while
#para calcular o fatorial. Após o cálculo, o programa imprime o resultado.


#This Python program calculates the factorial of a number provided by the user. It prompts
#the user to input the desired number and then uses a while loop to calculate the factorial.
#After the calculation, the program prints the result.