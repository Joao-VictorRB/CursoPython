palavras = ("banana", "computador", "cachorro", "livro", "carro", "mesa", "cadeira", "prato")

for p in palavras:
    print('\n Na palavra {} temos: '.format(p.upper()),end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end='')

# Este programa percorre uma lista de palavras e, para cada uma delas, imprime as vogais presentes.
# As palavras são exibidas em letras maiúsculas, seguidas pelas vogais encontradas, sem separar por
# linha, e considerando tanto letras minúsculas quanto maiúsculas.


# This program iterates through a list of words and, for each one, prints the vowels present. The words
# are displayed in uppercase, followed by the vowels found, without line breaks, and considering both
# lowercase and uppercase letters.