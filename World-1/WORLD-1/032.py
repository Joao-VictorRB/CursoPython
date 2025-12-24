from datetime import date

print('Vamos descobrir se o ano é bissexto, digite algum ano: ',end='')
ano= int(input())


if ano %4 and  ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto'.format(ano))

else:
    print('Não é um ano bissexto')