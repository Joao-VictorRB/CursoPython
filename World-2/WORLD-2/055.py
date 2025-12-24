lista_peso = []

for c in range (1,6):
    print('Peso da {}° pessoa: '.format(c),end='')
    peso = float(input())

    lista_peso.append(peso)

New_lista = sorted(lista_peso)

print('O maoir peso das 5 pessoas é: {}kg'.format(New_lista[4]))
print('O menor peso das 5 pessoas é: {}kg'.format(New_lista[0]))

# Este programa em Python permite que o usuário insira o peso de cinco
# pessoas. Em seguida, ele armazena esses pesos em uma lista e os organiza 
# em ordem crescente. Ao fazer isso, o programa identifica o menor e o maior
# peso da lista. Por fim, ele imprime esses valores, fornecendo ao usuário uma
# visão clara dos extremos da distribuição de pesos das cinco pessoas.


# This Python program allows the user to input the weight of five people. Then, it stores
# these weights in a list and sorts them in ascending order. By doing so, the program
# identifies the smallest and largest weight from the list. Finally, it prints out these
# values, providing the user with a clear view of the extremes of the weight distribution
# among the five people.