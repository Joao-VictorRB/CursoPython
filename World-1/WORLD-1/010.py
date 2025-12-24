print('Digite qual é o valor que você tem: R$ ',end='')
v=float(input())

#considerando que o dólar está R$ 3,27

print('Você consegue comprar U${:.2f} com esse valor'.format(v/3.27))