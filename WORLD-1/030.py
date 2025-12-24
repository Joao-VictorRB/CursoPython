print('Digite qualquer número inteiro: ',end='')
n =int(input())

p= n%2

if p == 0:
    print('{} é par'.format(n))

else:
    print('{} é ímpar'.format(n))
