cont_idade = Qtd_M = Qtd_F20 = 0

while True:
    print('Digite a idade: ',end='')
    idade = int(input())

    print('Digite o sexo [M/F]: ',end='')
    sexo = input().upper().strip()
    
    while sexo[0] != 'M' and sexo[0] != 'F':
        print('Valor inválido, tente novamente!')
        print('Digite o sexo [M/F]: ',end='')
        sexo = input().upper().strip()

    if idade > 18:
        cont_idade += 1
    
    if sexo[0] == 'M':
        Qtd_M += 1
    
    elif idade < 20 and sexo[0] == 'F':
        Qtd_F20 += 1
      
    print('Deseja continuar [S/N]: ',end='')
    resp = input().upper().strip()
    
    while resp[0] != 'S' and resp[0] != 'N':
        print('Valor inválido, tente novamente!')
        print('Deseja continuar [S/N]: ',end='')
        resp = input().upper().strip()

    if resp[0] == 'N':
        break   

print('Quantidade de pessoas com mais de 20 anos: {}'.format(cont_idade))
print('Quantidade de homens cadastrados: {}'.format(Qtd_M))
print('Quantidade de Mulheres com menos de 20 anos: {}'.format(Qtd_F20))  

# Este programa coleta informações sobre a idade e o sexo de várias pessoas. Para cada pessoa,
# o programa solicita a idade e o sexo (M para masculino e F para feminino), validando a entrada
# do sexo. O programa mantém um contador de pessoas com mais de 18 anos, a quantidade de homens
# cadastrados e a quantidade de mulheres com menos de 20 anos. Após cada entrada, o usuário é
# perguntado se deseja continuar ou encerrar o programa. Quando o usuário escolhe encerrar, o
# programa exibe os totais calculados.


# This program collects information about the age and gender of several people. For each person,
# the program prompts for age and gender (M for male and F for female), validating the gender input.
# The program keeps a count of people over 18 years old, the number of males registered, and the
# number of females under 20 years old. After each entry, the user is asked if they want to continue
# or end the program. When the user chooses to end, the program displays the calculated totals.