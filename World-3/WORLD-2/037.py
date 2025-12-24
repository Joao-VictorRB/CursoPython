print('Digite um número inteiro: ',end='')
valor = int(input())

print('Escolh uma das bases de conversão:')
print('[1] BINÁRIO')
print('[2] OCTAL')
print('[3] HEXADECIMAL')
print('Digite aqui: ',end='')
menu = int(input())

if menu < 1 and menu > 3:
    print('Erro!!!')

elif menu == 1:
    print('O número {} em BINÁRIO é: {} '.format(valor, bin(valor)[2:]))

elif menu == 2:
   print('O número {} em OCTAL é: {} '.format(valor, oct(valor)[2:]))

else:
   print('O número {} em OCTAL é: {} '.format(valor, hex(valor)[2:]))


# O Programa de Conversão de Inteiros em Python foi desenvolvido para converter um
# número inteiro para diferentes bases (binária, octal ou hexadecimal), com base na
# escolha do usuário. O programa solicita que o usuário insira um número inteiro e,
# em seguida, apresenta um menu de opções de conversão. O usuário seleciona uma das
# bases, e o programa realiza a conversão conforme a escolha feita.
 
   
# The Integer Conversion Program in Python is designed to convert an integer to different
# bases (binary, octal, or hexadecimal), based on the user's choice. The program prompts the
# user to input an integer and then provides a menu of conversion options. The user selects
# one of the bases, and the program performs the conversion accordingly.