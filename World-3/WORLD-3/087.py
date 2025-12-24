dados = [[], [], []] 
somar = 0 

for i in range(1, 10):
    valores = int(input('Digite os valores da matriz (3x3):'))
    
    if valores % 2 == 0:
        somar += valores 
  
    if len(dados[0]) < 3:
        dados[0].append(valores)
    elif len(dados[1]) < 3:
        dados[1].append(valores)
    else:
        dados[2].append(valores)

maiorSegundaLinha = 0
for i in dados[1]:
    if i > maiorSegundaLinha:
        maiorSegundaLinha = i

print('[ {} ] [ {} ] [ {} ]'.format(dados[0][0], dados[0][1], dados[0][2]))
print('[ {} ] [ {} ] [ {} ]'.format(dados[1][0], dados[1][1], dados[1][2]))
print('[ {} ] [ {} ] [ {} ]'.format(dados[2][0], dados[2][1], dados[2][2]))

print('-='*30)

print('A soma de todos os valores pares digitados são: {}'.format(somar))
print('A soma dos valores da terceira coluna são: {}'.format(dados[0][2] + dados[1][2] + dados[2][2]))
print('O maior valor da segunda linha é o número: {}'.format(maiorSegundaLinha))

# Este código preenche uma matriz 3x3 com valores fornecidos pelo usuário. Ele calcula a soma dos números pares
# inseridos, encontra o maior valor da segunda linha da matriz e soma os valores da terceira coluna. O programa
# exibe a matriz preenchida e apresenta os resultados de forma organizada.


# This code fills a 3x3 matrix with values provided by the user. It calculates the sum of the even numbers entered,
# finds the highest value in the second row of the matrix, and sums the values of the third column. The program 
# displays the filled matrix and presents the results in an organized way.