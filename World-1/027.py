print('Digite seu nome completo: ',end='')
n =input().upper()

first = n.split() [0]
last = n.split()[-1]
print('='*30)

print('Seu nome completo: {}\nPrimeiro nome: {} \nÚltimo nome: {} '.format(n,first,last))