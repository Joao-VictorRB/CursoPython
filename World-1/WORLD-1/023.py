
print('Digite um número entre 0 e 9999: ',end='')
v = int((input()))

m = v//1000%10
c= v//100%10
d = v//10%10
u = v//1%10

print('Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(m,c,d,u))