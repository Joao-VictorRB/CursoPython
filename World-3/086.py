dados = [[],[],[]]

for i in range(1,10):
    valores = int(input('Digite os valores da matriz (3x3):'))

    if len(dados[0]) < 3:
        dados[0].append(valores)

    elif  len(dados[0]) == 3 and len(dados[1]) < 3 :
        dados[1].append(valores)
    else:
        dados[2].append(valores)

print('[ {} ] [ {} ] [ {} ]'.format(dados[0][0], dados[0][1], dados[0][2],))
print('[ {} ] [ {} ] [ {} ]'.format(dados[1][0], dados[1][1], dados[1][2],))
print('[ {} ] [ {} ] [ {} ]'.format(dados[2][0], dados[2][1], dados[2][2],))

# Este código solicita ao usuário que insira 9 valores, preenchendo uma matriz 3x3 (uma lista composta por 3 listas,
# cada uma com até 3 elementos). Os valores são inseridos linha por linha. O código verifica se as três linhas da
# matriz estão completamente preenchidas, exibindo a matriz de forma segura. Caso alguma linha não seja completamente
# preenchida, o programa avisa ao usuário. O código também garante que os índices da matriz não sejam acessados
# incorretamente, evitando erros.


# This code asks the user to input 9 values, filling a 3x3 matrix (a list composed of 3 lists, each with up to 3
# elements). The values are entered row by row. The code checks if all three rows of the matrix are fully filled
# and displays the matrix safely. If any row is not fully filled, the program informs the user. It also ensures
# that the matrix indices are not accessed incorrectly, preventing errors.