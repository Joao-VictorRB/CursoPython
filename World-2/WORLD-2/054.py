from datetime import date
data = date.today().year - 18

l1 = []
l2 = []

for c in range(1,8):
    print('Em que ano a {}° pessoa nasceu: '.format(c),end='')
    ano = int((input()))

    if ano <= data:
        
        l1.append(ano)

    else:

        l2.append(ano)
    
print('Um total de {} pessoas JÁ atingiram a maioridade'.format(len(l1)))

print('Um total de {} pessoas NÃO atingiram a maioridade'.format(len(l2)))

# Este programa Python calcula o ano em que uma pessoa atinge a maioridade
# (18 anos atrás do ano atual) e solicita ao usuário sete vezes que insira
# o ano de seu aniversário. Com base na entrada do usuário, ele classifica os
# anos de aniversário em duas listas: uma para as pessoas que já atingiram a
# maioridade e outra para as que ainda não atingiram. No final, imprime o total
# de pessoas em cada categoria.


# This Python program calculates the year when a person reaches adulthood
# (18 years ago from the current year) and asks the user seven times to input
# their birth year. Based on the user input, it sorts the birth years into two
# lists: one for people who have already reached adulthood and another for those
# who have not. Finally, it prints the total number of people in each category.