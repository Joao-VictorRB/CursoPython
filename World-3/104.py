def leiaInt(msg):
    ok = False
    valor = 0

    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido. \033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

# A função leiaInt(msg) solicita ao usuário que insira um número inteiro. Ela repete a solicitação até que o usuário 
# forneça um valor válido. Se o valor inserido não for um número inteiro (ou seja, não for numérico), uma mensagem de erro
# é exibida, e o programa solicita novamente a entrada. Quando um número inteiro válido é informado, a função retorna o 
# valor e sai do loop. O parâmetro msg permite personalizar a mensagem de solicitação. No exemplo, a função é chamada para
# pedir ao usuário "Digite um número" e, em seguida, imprime o número informado pelo usuário.


# The function leiaInt(msg) prompts the user to enter an integer. It repeatedly asks for input until the user provides a 
# valid integer. If the input is not a valid integer (i.e., not numeric), an error message is displayed, and the program 
# prompts the user again. When a valid integer is entered, the function returns the value and exits the loop. The msg 
# parameter allows customizing the prompt message. In the example, the function is called to ask the user to "Digite um 
# número" (Enter a number) and then prints the number entered by the user.