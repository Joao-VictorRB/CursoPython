print('Digite uma frase: ',end='')
f = input().lower().strip()

a = f.count('a')
first = f.find('a')+1
last = f.rfind('a')+1

print('='*30)

print('''Quantas vezes apareceu a letra A: {}
\nPrimeira vez que apareceu a letra A: {}
\nÚltma vez que apareceu a letra A: {}'''.format(a,first,last))