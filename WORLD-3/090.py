registro = {'nome':'','média':'','situação':''}

for i in range(0,1):
    nome = input('Digite o nome do aluno: ').strip()
    média = float(input(f'Digite a média do {nome}: '))

registro['nome'] = nome 
registro['média'] = média

if média > 5:

  registro['situação'] = 'Aprovado'

else:
   registro['situação'] = 'Reprovado'

print(f'Nome do aluno: {registro["nome"]}')
print(f'Média é igual a: {registro["média"]}')
print(f'Situação é igual a: {registro["situação"]}')
    
# Este programa permite registrar informações de um aluno, incluindo seu nome, média e situação (aprovado ou reprovado)
# com base na média. O programa solicita o nome e a média do aluno. Em seguida, compara a média: se for maior que 5,
# o aluno é considerado "Aprovado"; caso contrário, o aluno é "Reprovado". Após a avaliação, o programa exibe o nome
# do aluno, sua média e sua situação (aprovado ou reprovado) de maneira clara e organizada.


# This program allows registering a student's information, including their name, average grade, and status (approved or
# failed) based on the average. The program asks for the student's name and average grade. It then compares the average:
# if it is higher than 5, the student is considered "Approved"; otherwise, the student is "Failed". After the evaluation,
# the program displays the student's name, average grade, and status (approved or failed) in a clear and organized manner.