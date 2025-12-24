valores = []
resposta = ''

while True:

   print('Digite um valor: ',end='')
   v = int(input()) 

   if v in valores:
       print('Esse valor já está registrado')
       print('Deseja registrar outro valor [s/n]: ',end='')
       resposta = input().lower()

       if resposta == 'n':
           break
   else:

        valores.append(v)
        print('Deseja registrar outro valor [s/n]: ',end='')
        resposta = input()

        if resposta == 'n':
           break

print('O valores válidos da lista são: {}'.format(sorted(valores)))

# Este programa em Python solicita repetidamente que o usuário insira um valor inteiro e o adiciona a uma lista.
# Ele verifica se o valor já está presente na lista e, se estiver, notifica o usuário de que o valor já foi 
# registrado. O usuário é então perguntado se deseja inserir outro valor. O processo continua até que o usuário
# decida não inserir mais valores, digitando 'n'.

# Ao final, o programa exibe a lista dos valores válidos (únicos) inseridos pelo usuário, ordenada em ordem crescente.


# This Python program repeatedly asks the user to input an integer value and adds it to a list. It checks if the value
# is already present in the list, and if it is, it notifies the user that the value has already been recorded.
# The user is then asked if they want to enter another value. This process continues until the user decides not
# to enter any more values by typing 'n'.

# At the end, the program displays the list of valid (unique) values entered by the user, sorted in ascending order.