from random import randint
import time

def maior():
    Lista = []

    programa = randint(1,5)

    for i in range(programa):
        Qtd_Num_In_List = randint(0,6)

        for i in range(Qtd_Num_In_List):

            num = randint(0,10)
            Lista.append(num)
    
        print('Analisando Valores passados...')
        time.sleep(1)
        if not Lista:
            print('Foram informados 0 valores ao todo')
        else:
            print(f'{" ".join(map(str,Lista))} Foram informados {len(Lista)} valores ao todo.')
        time.sleep(1)
        if not Lista:
            print('O maior valor informado foi 0.')
        else:
            print(f'O maior valor passado foi {max(Lista)}')
        print('-='*30)
        Lista.clear()

maior()

# O código gera uma lista de números aleatórios e analisa o maior valor presente nela. Primeiramente, o programa define
# um número aleatório entre 1 e 5 para determinar quantas vezes ele irá executar o processo. Dentro de cada execução, ele
# gera um número aleatório entre 0 e 6, que define quantos números serão adicionados à lista. A cada ciclo, o código
# imprime a lista gerada, o total de valores informados e o maior valor presente na lista. Se a lista estiver vazia, é
# exibida uma mensagem informando isso. Ao final de cada ciclo, a lista é limpa, e o processo é repetido.


# The code generates a list of random numbers and analyzes the highest value in it. First, the program defines a random
# number between 1 and 5 to determine how many times it will run the process. Inside each run, it generates a random
# number between 0 and 6, which defines how many numbers will be added to the list. In each cycle, the code prints the
# generated list, the total number of values provided, and the highest value in the list. If the list is empty, a 
# message is shown indicating that. At the end of each cycle, the list is cleared, and the process repeats.