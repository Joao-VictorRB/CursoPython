print('Digite o valor do produto: R$ ',end='')
valor = float(input())

print('[1] A vista DINHEIRO / CHEQUE: 10% de desconto')
print('[2] A vista no CARTÃO: 5% de desconto')
print('[3] Em 2x NO CARTÃO: preço normal')
print('[4] 3x OU MAIS no cartão: 20% de juros')
print('Digite: ',end='')
menu = int(input())

if menu > 4 or menu < 0:
    print('Erro...')

elif menu == 1:
    print('Valor do produto: R${:.2f}'.format(valor-((10 * valor)/100)))

elif menu == 2:
    print('Valor do produto: R${:.2f}'.format(valor-((5 * valor)/100)))

elif menu == 3:
    print('Valor do produto em 2x: R${:.2f}'.format(valor/2))

else:
    print('Digite em quantas vezes no cartão: ',end='')
    x = int(input())
    
    if x < 3: 
        print('Erro...')
    
    else:
        print('Valor do produto em {}x: R${:.2f}'.format(x,(valor + ((20 * valor)/100))/x))
       
# O Programa de Opções de Pagamento em Python é um script projetado para calcular o preço
# final de um produto com base no método de pagamento selecionado pelo usuário. O programa
# solicita que o usuário insira o valor do produto e, em seguida, apresenta um menu de opções
# de pagamento, cada uma com suas respectivas taxas de desconto ou juros
 
        
# The Payment Options Program in Python is a script designed to calculate the final price of a
# product based on the user 's selected payment method. The program prompts the user to input the
# product value and then provides a menu of payment options, each with its corresponding discount
# or interest rates.