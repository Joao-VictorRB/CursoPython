def escrever(mensagem,):

    tamanho = int(len(mensagem))+2
    
    print('-' * tamanho)
    print(' ' + mensagem + '')
    print('-' * tamanho)



mensagem = 'Hello, World'

escrever(mensagem)

# O código define uma função chamada escrever, que recebe uma mensagem como entrada e a imprime dentro de uma borda de 
# traços. O comprimento da borda é calculado com base no tamanho da mensagem, garantindo que a borda seja um pouco maior
# do que a mensagem. A função imprime primeiro uma linha de traços acima da mensagem, em seguida a mensagem com espaços ao
# redor, e finalmente uma linha de traços abaixo, criando um visual organizado e destacado para a mensagem no console.


# The code defines a function called escrever, which takes a message as input and prints it inside a border of dashes.
# The length of the border is calculated based on the size of the message, ensuring the border is slightly larger than 
# the message. The function first prints a line of dashes above the message, then the message with spaces around it, and
# finally, a line of dashes below, creating an organized and highlighted appearance for the message in the console.