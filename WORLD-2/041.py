from datetime import date

print('Digite o seu ano de nascimento: ',end='')
data_nasc = int(input())

data = date.today().year
idade_categoria =  data - data_nasc 
idade = data - data_nasc 

print('O atleta tem {} anos.'.format(idade))

if idade_categoria >= 1 and idade_categoria <= 9:
    print('Categoria: MIRIM')

elif idade_categoria >= 10 and idade_categoria <= 14:
    print('Categoria: INFANTIL')

elif idade_categoria >= 15 and idade_categoria <= 19:
    print('Categoria: JUNIOR')

elif idade_categoria >= 20 and idade_categoria <= 25:
    print('Categoria: SÊNIOR')

else:
    print('Categoria: MASTER')


# O Programa de Categorização de Idade para Competições Desportivas é uma
# aplicação desenvolvida em Python que solicita o ano de nascimento do usuário
# e, com base nessa informação, determina a categoria adequada para participação
# em competições esportivas. As categorias incluem Mirim, Infantil, Júnior, Sênior
# e Máster, sendo definidas de acordo com critérios estabelecidos para cada faixa etária.


# The Age Categorization Program for Sports Competitions is a Python application that prompts
# the user for their year of birth and, based on this information, determines the appropriate
# category for participation in sports competitions. The categories include Mirim, Infantil,
# únior, Sênior, and Máster, defined according to established criteria for each age group.