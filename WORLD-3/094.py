dados = []
registros = {'Nome':'','Sexo':'','idade':''}
mulheres = []
IdadeAcimaMédia = []
média = 0

while True:
    nome = input('Digite o nome: ')
    sexo = input('Digite o sexo (M/F): ').upper()[0]

    while sexo != 'M' and sexo != 'F':
        print('Valor inválido !!')
        sexo = input('Digite o sexo (M/F): ').upper()
    
    idade = int(input('Digite a idade: '))
    média += idade
    resp = input('Deseja continuar (S/N):').upper()

    registros['Nome'] = nome
    registros['Sexo'] = sexo
    registros['idade'] = idade

    dados.append(registros.copy())
    
    registros['Nome'] = ''
    registros['Sexo'] = ''
    registros['Idade'] = ''

    if resp in 'N':
        break

média = média/ len(dados)

for m in range(len(dados)):
    if dados[m]['Sexo'] == 'F':
        mulheres.append(dados[m]['Nome'])

for m in range(len(dados)):
    if dados[m]['idade'] > média:
        IdadeAcimaMédia.append(dados[m])
        
print(f'Quantidade de pessoas cadastradas: {len(dados)}')
print('Idade média é: {:2f}'.format(média))
print(f'Todas as mulheres registradas: {mulheres}')
print(f'Pessoas com idade acima da média: {IdadeAcimaMédia}')

# Este código tem como objetivo realizar o cadastro de várias pessoas com nome, sexo e idade, armazenando essas informações
# em uma lista de dicionários. Em seguida, ele realiza algumas análises sobre os dados cadastrados, como calcular a média
# de idades, filtrar as mulheres cadastradas e listar as pessoas com idade superior à média. Ao final, o programa imprime
# algumas informações relacionadas a essas análises. 


# This code aims to register multiple people with their name, gender, and age, storing this information in a list of
# dictionaries. Then, it performs some analysis on the registered data, such as calculating the average age, filtering
# the registered women, and listing the people with an age above the average. In the end, the program prints some
# information related to these analyses.