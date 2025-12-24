print('Digiter o valor do seu salário: R$',end='')
s = float(input())

if s > 1250:
    new = ((s*10)/100)+s
    print('Seu novo salário será de {}'.format(new))

else: 
    new2 = ((s*15)/100)+s
    print('Seu novo salário será de {}'.format(new2))