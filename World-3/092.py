import datetime

ano_atual = datetime.datetime.now().year

dados = {'nome':'', 'ano_nasc':'','CTPS':'','anoContratacao':'','salario':'','aposentadoria':''}

dados['nome'] = input('Digite seu nome: ').strip()
dados['ano_nasc'] = int(input(f'{dados["nome"]}, digite seu ano de nascimento: '))
dados['CTPS'] = int(input('Digite sua carteira de trabalho (0 não tem): '))
 
if dados['CTPS'] == 0:

    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {int(ano_atual - dados["ano_nasc"])}')
    print(f'C.T.P.S.: {dados["CTPS"]}')
    
else:

    dados['anoContratacao'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = int(input('Digite seu salário: R$ '))
 
    aposentaodria = 35 - (ano_atual -  dados['anoContratacao']) + int(ano_atual - dados["ano_nasc"])
    dados['aposentadoria'] = aposentaodria
    print('-='*30)
    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {int(ano_atual - dados["ano_nasc"])}')
    print(f'C.T.P.S.: {dados["CTPS"]}')
    print(f'Ano de contratação: {dados["anoContratacao"]}')
    print(f'Salário: {dados["salario"]}')
    print(f'Aposentadoria: {dados["aposentadoria"]}')

# Este código coleta informações pessoais de um usuário, como nome, ano de nascimento, número da carteira de trabalho
# (CTPS), ano de contratação e salário. Se o usuário não possuir CTPS, ele exibe apenas o nome e a idade. Caso o usuário
# tenha CTPS, o código calcula o tempo restante até a aposentadoria com base na fórmula simplificada (35 anos após o ano
# de contratação). Em seguida, exibe todos os dados coletados, incluindo a idade, CTPS, ano de contratação, salário e
# o tempo restante até a aposentadoria, se aplicável.


# This code collects personal information from a user, such as name, birth year, work card number (CTPS), hiring year,
# and salary. If the user does not have a CTPS, it only displays the name and age. If the user has a CTPS, the code 
# calculates the remaining time until retirement based on a simplified formula (35 years after the hiring year). It then
# displays all collected data, including age, CTPS, hiring year, salary, and the remaining time until retirement,
# if applicable.