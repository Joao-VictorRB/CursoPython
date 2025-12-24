dados = []

while True:
    nome = input('Digite o nome do aluno: ')
    nota_1 = float(input('Digite a 1° nota: '))
    nota_2 = float(input('Digite a 2° nota: '))

    média = (nota_1 + nota_2) / 2

    dados.append([nome, nota_1, nota_2, média])

    resp = input('Deseja continuar [s/n]: ').lower()

    if resp in 'n':
        break

print('\n{:<4} {:<20} {:<6}'.format('N°', 'NOME', 'MÉDIA'))
print('-' * 40)

for i, l in enumerate(dados):
    print(f'{i:<4} {l[0]:<20} {l[3]:<6.2f}')  

while True:
    print('-' * 40)
    registro = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if registro == 999:
        break

    if registro >= 0 and registro < len(dados):
        print(f'Notas de {dados[registro][0]} são: [{dados[registro][1]}, {dados[registro][2]}]')
    else:
        print('Aluno não encontrado. Tente novamente.')

# Este programa permite o cadastro de alunos com suas respectivas notas e o cálculo da média de cada aluno.
# O processo ocorre em um loop onde o usuário insere o nome e as duas notas de cada aluno. Após o cadastro,
# o programa exibe uma lista com o nome e a média de todos os alunos cadastrados. O usuário pode continuar
# cadastrando alunos até decidir parar. Além disso, o programa oferece a opção de exibir as notas específicas
# de um aluno, com a possibilidade de interromper a consulta de notas a qualquer momento.


# This program allows the registration of students with their respective grades and calculates each student's average.
# The process happens in a loop where the user inputs the name and the two grades for each student. After registration,
# the program displays a list with the names and averages of all registered students. The user can continue adding
# students until they decide to stop. Additionally, the program provides the option to view specific student grades,
# with the ability to interrupt the grade lookup at any time.