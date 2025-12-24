numeros_por_extenso = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze",
"doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

print('Digite um número entre 0 a 20: ',end='')
n = int(input())

while n < 0 or n > 20 : #checando a resposta do usuário
    print('Digite um número entre 0 a 20: ',end='')
    n = int(input())

print('Você digitou o número {}'.format(numeros_por_extenso[n]))

# O programa solicita ao usuário que digite um número entre 0 e 20. Se o número fornecido
# estiver fora desse intervalo, ele continuará solicitando até que o usuário forneça um número
# válido. Em seguida, o programa imprime o número digitado por extenso.


# The program prompts the user to enter a number between 0 and 20. If the provided number is
# outside this range, it keeps asking until the user provides a valid number. Then, the program
# prints the entered number in words.