print('Digite o valor que será sacado R$: ',end='')
valor = int(input())
resto = 0

v_50 = v_20 = v_10 = v_1 = 0

if valor >= 50:    
  v_50 = valor//50 
  resto = valor - (v_50 * 50)

if valor >= 20 or resto >= 20:
   v_20 = resto // 20
   resto = resto - (v_20 * 20)

if valor >= 10 or resto >= 10:
   v_10 = resto // 10
   resto = resto - (v_10 * 10)

if valor >= 1 or resto >= 10:
   v_1 = resto 

print('==========Programa finalizado============')

if v_50 > 0:
   print('Total de {} cédulas de R$50'.format(v_50))
if v_20 > 0:
   print('Total de {} cédulas de R$20'.format(v_20))
if v_10 > 0:
   print('Total de {} cédulas de R$10'.format(v_10))
if v_1 > 0:
   print('Total de {} cédulas de R$1'.format(v_1))

# Este programa solicita ao usuário um valor em reais a ser sacado e calcula a quantidade mínima de
# cédulas necessárias para compor esse valor, usando cédulas de R$50, R$20, R$10 e R$1. O programa 
# faz isso dividindo o valor de saque pelas denominações das cédulas, começando pelas maiores (R$50)
# e subtraindo o valor correspondente até as menores (R$1). Ao final, o programa exibe a quantidade
# de cédulas de cada denominação necessária para completar o valor solicitado.


# This program prompts the user for a withdrawal amount in Brazilian reais and calculates the minimum
# number of banknotes required to compose that amount, using R$50, R$20, R$10, and R$1 banknotes. The
# program does this by dividing the withdrawal amount by the banknote denominations, starting with the
# largest (R$50) and subtracting the corresponding value down to the smallest (R$1). Finally, the program
# displays the number of banknotes of each denomination needed to complete the requested amount.