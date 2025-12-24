def notas(lista):
    """
    -> Função para calcular: quantidade de notas, maior nota, menor nota e média de alunos.
    :para lista: list onde será armazenada as informações da váriavel (resp).
    :return: dicionário com as respostas.
    """

    notas ={'Qtd Notas':'','Maior Nota':'','Menor Nota':'','Média':''}
    
    notas['Qtd Notas'] = len(lista)
    notas['Maior Nota'] =  max(lista)
    notas['Menor Nota'] = min(lista)
    notas['Média'] = sum(lista) / len(lista)

    return notas


lista = []
while True:
    resp = float(input('Digite a nota: '))
    lista.append(resp)

    sair = input('Deseja continuar: [s/n]: ').lower()
    if sair in 'n':
        break

print(notas(lista))
help(notas)

# A função notas(lista) tem o objetivo de calcular algumas informações sobre as notas dos alunos, como a quantidade de 
# notas, a maior nota, a menor nota e a média das notas. Ela recebe como parâmetro uma lista contendo as notas dos alunos.
# A função cria um dicionário, onde são armazenados os resultados dessas informações: quantidade de notas, maior e menor 
# nota, e a média das notas. O dicionário é então retornado. No código, o usuário insere as notas repetidamente até 
# decidir parar, e essas notas são armazenadas em uma lista, que é passada como argumento para a função notas para 
# calcular os dados. O resultado final é um dicionário com as informações calculadas.


# The function notas(lista) aims to calculate several details about the students' grades, such as the number of grades, 
# the highest grade, the lowest grade, and the average grade. It takes a list of grades as a parameter. The function 
# creates a dictionary to store the results of these calculations: the number of grades, the highest and lowest grades, 
# and the average grade. The dictionary is then returned. In the code, the user enters grades repeatedly until they decide
# to stop, and these grades are stored in a list, which is passed as an argument to the notas function to compute the 
# data. The final result is a dictionary with the calculated information.