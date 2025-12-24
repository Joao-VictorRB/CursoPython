from time import sleep

c = (
     '\033[m', # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 1 - verde
     '\033[0;30;43m', # 1 - amarelo
     '\033[0;30;44m', # 1 - azul
     '\033[0;30;45m', # 1 - roxo
     '\033[7;30m', # 1 - branco
);


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6],end='')
    help(com)
    print(c[0],end='')
    sleep(2)


def título(msg,cor = 0):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('-=' * tam)
    print(f'  {msg}')
    print('-=' * tam)
    print(c[0],end='')
    sleep(1)

   
comando =''
while True:
    título('SISTEMA DE AJUDA PyHELP',2)
    comando = input('Função ou biblioteca >')
    if comando.upper == 'FIM':
        break
    else:
        ajuda(comando)
    título('ATÉ LOGO',1)

# O código implementa um sistema de ajuda interativo para consultar o manual de comandos e funções do Python. Ele utiliza 
# a biblioteca time para criar um pequeno atraso entre as mensagens exibidas. A função ajuda(com) exibe o manual de um 
# comando ou função, utilizando a função help(). Antes de mostrar o manual, ela chama a função título() para formatar e 
# exibir um título colorido com a descrição do comando. A função título() exibe uma mensagem formatada com bordas e uma 
# cor personalizada (escolhida de um conjunto de cores). O loop principal solicita ao usuário um comando ou biblioteca, e,
#  ao digitar o nome do comando, o sistema exibe seu manual. O loop continua até o usuário digitar "FIM", momento em que 
# o programa encerra.


# The code implements an interactive help system to query the manual of Python commands and functions. It uses the time 
# library to introduce a small delay between the displayed messages. The function ajuda(com) shows the manual of a given 
# command or function using the help() function. Before showing the manual, it calls the function título() to format and 
# display a colored title with the command description. The function título() displays a message with borders and a custom
# color (chosen from a set of colors). The main loop asks the user for a command or library, and upon entering the command
# name, the system displays its manual. The loop continues until the user types "FIM", at which point the program terminates.