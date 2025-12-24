print('Digite sua primeira nota: ',end='')
nota_1 = float(input())

print('Digite sua segunda nota: ',end='')
nota_2 = float(input())

media = (nota_1 + nota_2)/2

if media > 7:
    print(' Média: {}'.format(media))
    print('\033[1;32m APROVADO\033[m')

elif media >= 5 and media <= 6.9:
    print(' Média: {}'.format(media))
    print('\033[1;33mRECUPERAÇÃO\033[m')

else:
    print(' Média: {}'.format(media))
    print('\033[1;31mREPROVADO\033[m')

# O Programa de Avaliação de Desempenho Acadêmico é uma aplicação simples
# desenvolvida em Python para calcular a média de duas notas fornecidas pelo
# usuário, seguida da determinação do status acadêmico do aluno. O programa segue
# critérios padrão para avaliação, classificando o aluno como "Aprovado", "Em Recuperação"
# ou "Reprovado".
  
    
# The Academic Performance Evaluation Program is a simple Python application designed to calculate
# the average of two grades provided by the user, followed by determining the academic status of the
# student. The program follows standard evaluation criteria, classifying the student as "Approved," 
# "Under Recovery," or "Failed."