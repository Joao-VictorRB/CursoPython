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

def resumo(n=0,a=10,d=5):
   
    print(f'-'*30)
    print('RESUMO DO VALOR'.center(30))
    print(f'-'*30)

    print(f'Preço analisado: \t{padraoMonetario(n)}')
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'Metade do preço: \t{metade(n,True)}')
    print(f'{a}% de aumento: \t{aumentar(n,a,True)}')
    print(f'{d}% de redução: \t{diminuir(n,d,True)}')


