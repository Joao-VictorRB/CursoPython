print('Digite um número: ',end='')
n1 =float(input())

print('Digite outro número: ',end='')
n2 =float(input())

print('Digite mais um número: ',end='')
n3 =float(input())

lista=[n1,n2,n3]

print('O menor valor é: {}, e o maior valor é: {}'.format(min(lista),max(lista)))