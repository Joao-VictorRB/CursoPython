def fatorial(n,show=False):
    """
    -> Calcula o faotiral de um número.
    :para n: O número a ser calculado.
    :para show: (opcional) Mostrar ou não a conta.
    :return: valor fatorial de um número (n).
    """
       
    f = 1 
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f


print(fatorial(8, show=True))
help(fatorial)

# A função fatorial(n, show=False) calcula o fatorial de um número n. Ela recebe dois parâmetros: n, o número a ser 
# calculado, e show, que é opcional e, quando True, faz a função exibir a sequência da multiplicação (como 8 x 7 x 
# 6 x ...). O fatorial é calculado multiplicando-se os números de n até 1, e o resultado é armazenado na variável f, que
# é retornada ao final. Caso show seja True, a função imprime a operação passo a passo, caso contrário, apenas retorna o
# valor do fatorial sem mostrar o cálculo.


# The function fatorial(n, show=False) calculates the factorial of a number n. It takes two parameters: n, the number to
# be calculated, and show, which is optional and, when set to True, displays the multiplication sequence (like 8 x 7 x 6
# x ...). The factorial is calculated by multiplying the numbers from n down to 1, with the result stored in the variable
# f, which is returned at the end. If show is True, the function prints the operation step by step; otherwise, it simply
# returns the factorial value without showing the calculation.