soma = contador = 0

while True:
  print('Digite um número interiro [999 para finalizar]: ',end='')
  n = int(input())
  
  if n == 999:
    break

  soma += n
  contador += 1

print('Números digitados: {} | Soma entre eles: {}'.format(contador,soma))

# Este programa solicita ao usuário a inserção de números inteiros até que o número 999 seja digitado,
# indicando o fim da entrada. Para cada número inserido, o programa mantém um contador de quantos números
# foram digitados e calcula a soma desses números. Quando o número 999 é inserido, o programa termina e
# exibe o total de números digitados (excluindo 999) e a soma dos valores inseridos.


# This program prompts the user to enter integer numbers until the number 999 is entered, signaling the end
# of input. For each entered number, the program keeps a count of how many numbers have been entered and
# calculates their sum. When the number 999 is entered, the program ends and displays the total count of
# numbers entered (excluding 999) and the sum of the entered values.