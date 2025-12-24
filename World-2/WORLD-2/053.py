print('Digite sua frase: ',end='')
frase = input().lower().strip()

separado = frase.split()
junto = ''.join(separado)                      

inverso = ''

for l in range(len(junto)-1, -1, -1):
    inverso += junto[l]

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')
    
# Este programa em Python solicita ao usuário que insira uma frase.
# Em seguida, converte a frase para letras minúsculas e remove espaços
# em branco no início e no final. Depois disso, verifica se a frase é 
# igual ao seu reverso. Se for, imprime que é um palíndromo; caso contrário,
# imprime que não é um palíndromo.


# This Python program prompts the user to input a phrase. Then, it converts the
# phrase to lowercase and removes leading and trailing whitespaces. After that,
# it checks if the phrase is equal to its reverse. If it is, it prints that it is
# a palindrome; otherwise, it prints that it is not a palindrome.