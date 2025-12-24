from random import randint

num = ()

for c in range(0,6):
    valor_aleatorio = randint(1,100)
    num = num + (valor_aleatorio,)

sorted(num)

print('Números gerados: {}'.format(num))
print('Maior valor: {}'.format(max(num)))
print('menor valor: {}'.format(min(num)))

# O código gera uma tupla de 6 números aleatórios entre 1 e 100. Em seguida, 
# exibe os números gerados, o maior valor e o menor valor da tupla.


# The code generates a tuple of 6 random numbers between 1 and 100. It then 
# displays the generated numbers, the highest value, and thelowest value in the
# tuple.