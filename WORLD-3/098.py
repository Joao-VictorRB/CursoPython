def contador(inicio, fim, passo):
   
    print('A-', end=' ')
    for i in range(1, 11):
        print(f'{i} -', end=' ')
    print()
  
    print('B-', end=' ')
    for i in range(10, -1, -2):
        print(f'{i} -', end=' ')
    print()

    print('C-', end=' ')

    if inicio > fim and passo > 0: 
        lista_invertida = [inicio] + list(range(fim, inicio, passo))[::-1]
        print(" - ".join(map(str, lista_invertida)))

    elif passo < 0: 
        lista2 = list(range(inicio, fim, passo)) + [fim]
        print(" - ".join(map(str, lista2)))

    elif passo == 0:  
        lista3 = list(range(inicio, fim, -1)) + [fim]
        print(" - ".join(map(str, lista3)))

    else: 
        for i in range(inicio, fim, passo):
            print(f'{i} -', end=' ')
        print()



inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))
passo = int(input('Digite o valor de passo: '))

contador(inicio, fim, passo)

# Este programa solicita ao usuário três valores: inicial, final e passo, e realiza três contagens diferentes.
# A primeira imprime os números de 1 a 10, a segunda imprime de 10 a 0, pulando de 2 em 2, e a última é determinada
# pelos valores fornecidos pelo usuário. Se o passo for 0, ele é alterado para 1. Dependendo dos valores, a contagem
# pode ser crescente ou decrescente. O programa imprime os números com " - " entre eles.


# This program asks the user for three values: start, end, and step, and performs three different counts. The first 
# prints the numbers from 1 to 10, the second prints from 10 to 0, skipping 2 by 2, and the last one is determined
# by the user's input. If the step is 0, it is changed to 1. Depending on the values, the count can be increasing or
# decreasing. The program prints the numbers with " - " in between.