contador = 0
media = 0

lista = []

r = 'S'

while r == 'S':
 print('Digite um valor inteiro: ',end='')
 valor = int(input())

 lista.append(valor)
 media += valor

 contador += 1
 lista.sort()

 print('Deseja continuar [S/N] : ',end='')
 r = input().upper().strip()
 r = r[0] 

 if r == 'N':
  print('Média: {}'.format(media/contador))
  print('Maior: {}'.format(lista[-1]))
  print('Menor: {}'.format(lista[0]))

# Este programa solicita ao usuário a inserção de valores inteiros repetidamente até que
# o usuário escolha parar. Para cada valor inserido, o programa atualiza a média dos valores,
# identifica o maior e o menor valor digitado até o momento, e mantém uma lista ordenada dos
# valores. Após cada entrada, o programa exibe a média, o maior e o menor valor, e pergunta
# ao usuário se deseja continuar ou encerrar o programa.


# This program repeatedly prompts the user to enter integer values until the user chooses to stop.
# For each entered value, the program updates the average of the values, identifies the highest and
# lowest values entered so far, and maintains a sorted list of the values. After each entry, the
# program displays the average, the highest, and the lowest value, and asks the user if they wish
# to continue or end the program.