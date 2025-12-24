import time

print('Digite o valor da casa: ',end='')
valor_casa = float(input())

print('Digite o valor do seu salário: ',end='')
valor_salario = float(input())

print('Quantos anos de financiamento: ',end='')
tempo_pagar = int(input())

salario_30 = (30*valor_salario)/100

prestacao_mensal = valor_casa/(tempo_pagar*12)

print('Calculando...')
time.sleep(2)

if prestacao_mensal <= salario_30:
    print('O financiamento desse empréstimo bancário foi\033[1;32m APROVADO \033[m')
    print('Valor da prestação mensal: R${:.2f}'.format(prestacao_mensal))
else:
    print('Empréstimo bancário \033[1;31m RECUSADO \033[m')


# Desenvolvi um programa para calcular a elegibilidade de um empréstimo bancário,
# levando em consideração variáveis como o valor do imóvel, o período de pagamento 
# desejado e a renda mensal do solicitante. O programa estabeleceu um limite de 30% 
# da renda mensal como critério para a aprovação do empréstimo.


# I developed a program to calculate the eligibility for a bank loan, considering variables
# such as the property value, the desired repayment period, and the applicant's monthly income.
# The program established a limit of 30% of the monthly income as a criterion for loan approval.