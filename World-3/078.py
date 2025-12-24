valores = []

for v in range (1,6):

    print('Digite {}° valor: '.format(v),end='')
    valor = int(input())

    valores.append(valor)
    
print('Você digitou os valores: {}'.format(valores))
print('Maior valor na lista: {}| Nas posições: '.format(max(valores)),end='')

for i, n in enumerate(valores):
    if n == max(valores):
        print(f'{i}...',end='')

print()

print('Menor valor na lista: {}| Nas posições: '.format(min(valores)),end='')

for i, n in enumerate(valores):
    if n == min(valores):
        print(f'{i}...',end='')
print()

# Este código solicita ao usuário que insira 5 números inteiros e armazena esses valores em uma lista.
# Em seguida, ele calcula e exibe o maior e o menor valor dessa lista, junto com as suas respectivas
# posições, considerando a contagem de posições a partir de 1.


# This code asks the user to input 5 integer numbers and stores these values in a list. It then calculates
# and displays the largest and smallest values from the list, along with their respective positions,
# considering positions starting from 1.