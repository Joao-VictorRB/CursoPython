Gastos = 0
Qtd_1000 = 0

nome_barato = ''
valor_barato = None

while True:
  print('Digite o nome do produto: ',end='')
  nome = input().capitalize().strip()
  print('Digite o valor do produto: ',end='')
  valor = float(input())

  Gastos += valor
  
  if valor > 1000:
    Qtd_1000+= 1
  
  if valor_barato is None or valor < valor_barato:

    nome_barato = nome
    valor_barato = valor
  
  print('Deseja continuar [S/N]: ',end='')
  resp = input().upper().strip()

  while resp[0] != 'S' and resp[0] != 'N':
    print('Valor inválido, tente novamente!')
    print('Deseja continuar [S/N]: ',end='')
    resp = input().upper().strip()

  if resp[0] == 'N':
    break

print('============Programa encerrado================')
print('Total gasto: {:.2f}'.format(Gastos))
print('Quantidade de produtos que custam mais de R$1000: {}'.format(Qtd_1000))
print('Nome do produto mais barato: {}'.format(nome_barato))

# Este programa solicita ao usuário o nome e o valor de vários produtos, e continua a coletar dados até que
# o usuário escolha parar. O programa mantém um total dos gastos, conta quantos produtos custam mais de R$100
# 0 e identifica o nome do produto mais barato inserido. Ao final, o programa exibe o total gasto, a quantidade
# de produtos que custam mais de R$1000 e o nome do produto mais barato.


# This program prompts the user for the name and value of various products, and continues collecting data until
# the user chooses to stop. The program keeps a running total of expenses, counts how many products cost more 
# than R$1000, and identifies the name of the cheapest product entered. At the end, the program displays the
# total spent, the number of products costing more than R$1000, and the name of the cheapest product.