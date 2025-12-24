contador = 0

valor = 0

lista = 0

while valor != 999:

  print('Digite um número inteiro ou 999 para finalizar : ',end='')
  valor = int(input())
  
  lista += valor
  contador += 1

print('Números digitados: {} | Resultado: {}'.format(contador - 1, lista - 999))

# Este programa solicita ao usuário números inteiros até que o número 999 seja digitado.
# A cada entrada, o número é somado a um acumulador e o contador de entradas é incrementado.
# Quando o número 999 é digitado, o programa exibe a quantidade total de números digitados
# (excluindo o 999) e a soma total desses números.


# This program prompts the user to enter integer numbers until the number 999 is input. Each
# entered number is added to an accumulator, and the entry count is incremented. When the number
# 999 is entered, the program displays the total count of numbers entered (excluding 999) and the
# total sum of these numbers.