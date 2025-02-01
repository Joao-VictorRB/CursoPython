def padraoMonetario(n):
    return f'R${n:2f}'.replace(".",",")


def metade(n, s= False):
    n = n/2
    if s == True:
        return padraoMonetario(n)
    else:
        return n

def dobro(n, s=False):
    n = n*2
    if s == True:
        return padraoMonetario(n)
    else:
        return n 

def aumentar(n,a,s= False):
    n = n + ((n*a)/100)
    if s == True:     
        return padraoMonetario(n)
    else:
        return n 

def diminuir(n,d,s=False):
    n = n - ((n*d)/100)
    if s == True:       
        return padraoMonetario(n)
    else:
        return n

def resumo(n,a,d):

    Espacotxt = f'-='*len('RESUMO DO VALOR')
    print(f'{Espacotxt}')
    print('       RESUMO DO VALOR   ')
    print(f'{Espacotxt}')

    print(f'Preço analisado:....{padraoMonetario(n)}')
    print(f'Dobro do preço:.....{dobro(n,True)}')
    print(f'Metade do preço:....{metade(n,True)}')
    print(f'{a}% de aumento:.....{aumentar(n,a,True)}')
    print(f'{d}% de redução:.....{diminuir(n,d,True)}')