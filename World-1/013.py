print('Digite o valor do seu salário atual: ',end='')
v=float(input())

print('Seu novo salário será de R${:.2f}'.format(v+(15*v)/100))