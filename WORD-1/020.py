from random import shuffle

print('Digite o nome do primeiro aluno: ', end='')
a1 = input()
print('Digite o nome do segundo aluno: ', end='')
a2 = input()
print('Digite o nome do terceiro aluno: ', end='')
a3 = input()
print('Digite o nome do quarto aluno: ', end='')
a4 = input()

lista = [a1, a2, a3, a4]

shuffle(lista)

print('A sequência é a seguinte: {}'.format(lista))
