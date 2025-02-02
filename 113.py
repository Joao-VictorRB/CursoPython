def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('\n\033[31mERRO! valor inválido, tente novamente!!!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31m Usuário preferiu não digitar esse número \033[m')
            return 0
        else:
            return n 
        
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print('\n\033[31mERRO! valor inválido, tente novamente!!!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31m Usuário preferiu não digitar esse número \033[m')
            return 0
        else:
            return n 


i = leiaInt('Digite um número inteiro: ')
f = leiafloat('Digite um número float:')
print(f'Você acabou de digitar o número inteiro {i} e o real {f}')
