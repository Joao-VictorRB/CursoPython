dados = []

while True:
    nome = input('Digite o nome:')
    peso = float(input('Digite o peso:'))  

    dados.append([nome, peso])
    resp = input('Deseja continuar [s/n]:').lower()

    if resp in 'n':
        break

    print('-='*30)

leves = []
pesados = []

for p in dados:

    if not leves:
        leves.append(p)

    elif p[1] < leves[0][1]:  
        leves = [p] 

    elif p[1] == leves[0][1]:    
        leves.append(p)
    
    if not pesados:
        pesados.append(p)

    elif p[1] > pesados[0][1]:  
        pesados = [p] 

    elif p[1] == pesados[0][1]:    
        pesados.append(p)

print('Total de cadastros: {}'.format(len(dados)))
print('As pessoas mais pesadas são: {}. Pesando {}Kg'.format(', '.join([p[0] for p in pesados]),pesados[0][1]))
print('As pessoas mais leves são: {}. Pesando {}Kg'.format(', '.join([p[0] for p in leves]),leves[0][1]))
   
# Este código permite ao usuário cadastrar nomes e pesos de várias pessoas, armazenando essas informações em uma lista
# chamada dados. O código continua a perguntar pelo nome e peso até que o usuário decida parar, respondendo "n" quando
# perguntado se deseja continuar. Após o cadastro, o código determina as pessoas mais leves e mais pesadas, armazenando
# essas informações nas listas leves e pesados, respectivamente. Ao final, ele imprime o total de cadastros e os nomes
# das pessoas mais leves e mais pesadas, junto com seus respectivos pesos.


# This code allows the user to register names and weights of several people, storing this information in a list called
# dados. The code keeps asking for names and weights until the user decides to stop by answering "n" when asked if they
# want to continue. After registration, the code determines the lightest and heaviest people, storing this information
# in the lists leves and pesados, respectively. Finally, it prints the total number of registrations and the names of
# the lightest and heaviest people along with their respective weights.