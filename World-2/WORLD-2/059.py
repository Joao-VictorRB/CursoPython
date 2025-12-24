lista = []
r_menu = 0

print('Digite o 1° valor: ',end='')
p1 = int(input())
print('Digite o 2° valor: ',end='')
p2 = int(input())

while r_menu != 5:
 
 print('--------- MENU ---------')
 print('[1] Somar')
 print('[2] Multiplicar')
 print('[3] Maior')
 print('[4] Novos números')
 print('[5] Sair do programa')
 print('------------------------')
 print('Digite: ',end='')
 r_menu = int(input())

 if r_menu == 1:

    print('A soma entre {} + {} = {}'.format(p1,p2, p1+p2))
 
 elif r_menu == 2:
    
    print('A multiplicação entre {} x {} = {}'.format(p1,p2, p1*p2))

 elif r_menu == 3:
    
    lista.append(p1)
    lista.append(p2)
    print('O maior valor entre {} e {} = {}'.format(p1, p2, max(lista)))
 
 elif r_menu == 4:
    
    print('Digite o 1° valor: ',end='')
    p1 = int(input())
    print('Digite o 2° valor: ',end='')
    p2 = int(input())

print('Programa finalizado !!!')

#Este programa Python permite ao usuário realizar diversas operações matemáticas com dois valores.
#Ele apresenta um menu com opções para somar, multiplicar, encontrar o maior valor entre os dois números,
#inserir novos números ou sair do programa. O programa continua executando até que o usuário escolha a
#opção para sair.


#This Python program allows the user to perform various mathematical operations with two values. It presents
#a menu with options to add, multiply, find the largest value between the two numbers, input new numbers, or
#exit the program. The program continues running until the user chooses the option to exit.