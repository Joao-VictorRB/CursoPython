print('digite um número inteiro: ',end='')
n = int(input())

contador = 0

f0 = 0
f1 = 1

lista = []

lista.append(f0)
lista.append(f1)

while contador < n - 2:
    
 s = f0 + f1 

 lista.append(s)
 
 f0 = f1
 f1 = s
 
 contador += 1

print(lista)

# Este programa solicita ao usuário um número inteiro 'n' e gera os primeiros 'n' termos da sequência
# de Fibonacci. Inicialmente, a sequência começa com 0 e 1. O programa calcula os números subsequentes
# como a soma dos dois números anteriores e os adiciona a uma lista. Após gerar os 'n' termos, o programa
# exibe a lista completa da sequência.


# This program prompts the user for an integer 'n' and generates the first 'n' terms of the Fibonacci sequence.
# The sequence starts with 0 and 1. The program computes subsequent numbers as the sum of the two preceding
# numbers and appends them to a list. After generating 'n' terms, the program displays the complete list of the
# sequence.