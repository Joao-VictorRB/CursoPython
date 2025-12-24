print('Digite sua expressão: ',end='')
expressao = input()

pilha = []

for s in expressao:
    if s == '(':
        pilha.append('(')
    
    elif s == ')':

        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

# O código verifica se os parênteses em uma expressão estão balanceados. Ele percorre a expressão, utilizando
# uma pilha para verificar se cada parêntese de abertura tem um correspondente de fechamento. Se todos os
# parênteses estiverem corretamente balanceados, a expressão é válida; caso contrário, é inválida.


# The code checks if the parentheses in an expression are balanced. It uses a stack to ensure each opening
# parenthesis has a corresponding closing parenthesis. If all parentheses are properly balanced, the expression
# is valid; otherwise, it's invalid.