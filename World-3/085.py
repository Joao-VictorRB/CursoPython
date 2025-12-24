dados = [[],[]]

for i in range(1,8):
    valores = int(input('Digite {}° número:'.format(i)))

    if valores % 2 == 0:
        dados[0].append(valores)
    else:
        dados[1].append(valores)

print('Valores pares: {}'.format(sorted(dados[0])))
print('Valores ímpares: {}'.format(sorted(dados[1])))

# Este código solicita ao usuário que digite 7 números, um por vez. Para cada número digitado, ele verifica se o
# número é par ou ímpar. Se for par, o número é adicionado à lista dados[0], e se for ímpar, ele é adicionado à
# lista dados[1]. Ao final, o programa exibe as duas listas de números (pares e ímpares) ordenadas de forma crescente.


# This code prompts the user to enter 7 numbers, one at a time. For each number entered, it checks whether the number
# is even or odd. If it is even, the number is added to the list dados[0], and if it is odd, it is added to the list
# dados[1]. In the end, the program displays both lists of numbers (even and odd) sorted in ascending order.