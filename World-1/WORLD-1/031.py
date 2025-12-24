print('Digite a distância da vigem em km: ',end='')
v=float(input())


if v <= 200:

    print('O valor da su passagem ficou R${}'.format(v*0.50))

else:
    print('O valor da sua passagem ficou R${}'.format(v*0.45))