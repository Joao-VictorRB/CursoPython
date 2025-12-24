soma_idade = 0
media = 0

nome_homem_velho = ''
idade_homem_velho = 0

tot_mulher20 = 0

for p in range(1,3):
   print('----- PESSOA {}° -----'.format(p))
   print('Nome: ',end='')
   nome = str(input()).strip().upper()
   print('Idade: ',end='')
   idade = int(input())
   print('Sexo (M/F): ',end='')
   sexo = str(input()).lower()

   soma_idade += idade

   if p == 1 and sexo == 'm':

      nome_homem_velho =  nome
      idade_homem_velho = idade
    
   if sexo == 'm' and idade > idade_homem_velho :
       
      nome_homem_velho = nome
      idade_homem_velho = idade
    
   if sexo == 'f' and idade > 20:
       
      tot_mulher20 += 1
       
print('A média de idade é: {}'.format(soma_idade/4))
print('O homem mais velho se chama {} e tem {} anos'.format(nome_homem_velho,idade_homem_velho))
print('Tem um total de {} mulheres com menos de 20 anos'.format(tot_mulher20))

# Este programa em Python solicita informações sobre duas pessoas, incluindo nome, idade e sexo.
# Em seguida, ele calcula a média das idades das duas pessoas e identifica o homem mais velho entre
# elas. Além disso, conta quantas mulheres têm mais de 20 anos. Ao final, o programa imprime a média
# das idades, o nome e a idade do homem mais velho, e o total de mulheres com menos de 20 anos.


# This Python program requests information about two individuals, including their name, age, and gender.
# Then, it calculates the average age of the two individuals and identifies the oldest man among them.
# Additionally, it counts how many women are over 20 years old. Finally, the program prints the average
# age, the name and age of the oldest man, and the total number of women under 20 years old.        