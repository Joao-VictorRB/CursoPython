def padraoMonetario(n):
    return f'R${n:.2f}'.replace(".",",")


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
