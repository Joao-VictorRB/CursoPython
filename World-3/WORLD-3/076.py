produtos = ("Arroz", 20.50, "Feijão", 7.80, "Macarrão", 5.25, "Azeite", 15.90, "Leite", 4.50, "Café", 8.90,
            "Açúcar", 3.20, "Sal", 2.50, "Farinha de Trigo", 4.75, "Óleo", 6.30)

print('-' * 43)
print(' ' * 10, 'LISTAGEM DE PREÇOS')
print('-' * 43)

comp_max_produto = max(len(produto) for produto in produtos[0::2]) 
linha = ''

for c in range(0, len(produtos)):
    
    if c % 2 == 0:
        print('{:.<30}'.format(produtos[c]),end='')
    else:
        print('R${:>6.2f}'.format(produtos[c]))
    

# Este programa exibe uma lista de produtos junto com seus preços em uma tabela formatada. Ele percorre
# uma tupla contendo os nomes dos produtos e seus respectivos preços. Os nomes dos produtos são alinhados
# à esquerda, e os preços são alinhados à direita com o símbolo "R$". O programa garante que as colunas
# sejam organizadas de forma limpa e formatada de maneira consistente, tornando fácil a leitura dos nomes
# dos produtos e seus respectivos preços.   
 
 
# This program displays a list of products along with their prices in a formatted table. It iterates through
# a tuple containing product names and their corresponding prices. The product names are aligned to the left,
# and the prices are aligned to the right with a "R$" symbol. The program ensures that the columns are neatly
# organized and consistently formatted, making it easy to read the product names and their respective prices.