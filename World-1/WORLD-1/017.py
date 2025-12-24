from math import hypot

print('Digite o valor do cateto oposto: ',end='')
co=float(input())
print('Digite o valor do cateto adjacente: ',end='')
ca=float(input())

print('O valor da hipotenusa é {:.2f}'.format(hypot(co,ca)))