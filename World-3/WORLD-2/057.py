print('Digite seu sexo (M/F): ',end='')
sexo = str(input()).upper().strip() [0]

while sexo != 'M' and sexo != 'F':
    
    print('Dado inválido. Digite seu sexo novamente (M/F): ',end='')
    sexo = str(input()).upper().strip() [0]

print('Fim !!!')

#Este programa em Python solicita ao usuário que insira seu sexo (masculino ou feminino)
#através de uma entrada de texto. Em seguida, ele verifica se o sexo inserido é válido, ou
#seja, se é 'M' para masculino ou 'F' para feminino. Se a entrada não for válida, o programa
#exibe uma mensagem de erro e solicita que o usuário insira o sexo novamente. Isso continua
#até que o usuário insira um sexo válido. Após a entrada ser válida, o programa imprime "Fim!!!"
#e encerra a execução.


#This Python program prompts the user to input their gender (male or female) using a text input.
#Then, it checks if the entered gender is valid, i.e., if it is 'M' for male or 'F' for female.
#If the input is not valid, the program displays an error message and asks the user to input the
#gender again. This process continues until the user inputs a valid gender. After the input is valid,
#the program prints "End!!!" and terminates.