print('Digite o primeiro termo da PA: ', end='')
primeiro_termo = int(input())
print('Digite a razão da PA: ', end='')
razao = int(input())

lista = []

for i in range(10):
 pa = primeiro_termo + i  * razao
 lista.append(str(pa))
 
print(' > '.join(lista))

# Este código interativo em Python foi desenvolvido para gerar os primeiros 10
# termos de uma Progressão Aritmética (PA), com base no primeiro termo e razão
# fornecidos pelo usuário. Utilizando um loop for, o programa calcula cada termo
# da PA e os armazena em uma lista. A sequência resultante é impressa, destacando
# a natureza interativa e educativa do código.


# This interactive Python code was developed to generate the first 10 terms of an
# Arithmetic Progression (AP) based on user-provided first term and common difference.
# Using a for loop, the program calculates each term of the AP and stores them in a list.
# The resulting sequence is then printed, highlighting the interactive and educational
# nature of the code