print('Primeiro termo: ',end='')
p1 = int(input())

print('Razão da PA: ',end='')
r = int(input())

termo = p1
contador = 1
total = 0
mais = 10

while mais != 0:

   total = total + mais

   while contador <= total:
      print('{} > '.format(termo),end='')
      termo += r
      contador += 1

   print('Pausa')
   print('Quantos temos mais você quer mostrar: ',end='')
   mais = int(input())

print('Programa finalizado com um total de: {} termos'.format(total))

# Este programa gera e exibe termos de uma Progressão Aritmética (PA) com base no primeiro termo
# e na razão fornecidos pelo usuário. Inicialmente, o programa exibe os primeiros 10 termos da PA.
# Em seguida, o usuário pode optar por continuar exibindo mais termos conforme desejado. O programa
# continua a solicitar ao usuário quantos termos adicionais ele gostaria de ver até que o usuário
# escolha não exibir mais termos. Ao final, o programa exibe o total de termos mostrados.


# This program generates and displays terms of an Arithmetic Progression (AP) based on the first term
# and the common difference provided by the user. Initially, the program displays the first 10 terms
# of the AP. Then, the user can choose to continue displaying additional terms as desired. The program
# keeps asking the user how many more terms they want to see until the user decides to stop. Finally, 
# the program displays the total number of terms shown.