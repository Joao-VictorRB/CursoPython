num = (int(input('Digite o 1° número: ')),
       int(input('Digite o 2° número: ')),
       int(input('Digite o 3° número: ')),
       int(input('Digite o 4° número: ')))

print('Você digitou os seguintes números: {}'.format(num))

print('Nessa tupla existem {} número 9'.format(num.count(9)))
if 3 in num:
    print('O número 3 apareceu pela primeira vez na posição {}'.format(num.index(3) + 1))
else:
    print('O número 3 não apareceu na tupla')

for i  in num:
    if i % 2 == 0:
     print('Os números pares foram os seguintes: {}'.format(i))

# Este código tem como objetivo solicitar que o usuário insira 4 números inteiros, armazená-los em uma tupla e,
# em seguida, realizar algumas operações para analisar e exibir informações sobre os números inseridos.


# This code aims to prompt the user to enter 4 integer numbers, store them in a tuple, and then perform several
# operations to analyze and display information about the entered numbers.