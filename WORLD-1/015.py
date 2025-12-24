print('Quantos Km foram percorridos: ',end='')
v1= float(input())
print('Quantos dias foram alugado: ',end='')
v2=int(input())

# R$60 o dia e R$0.15 por km rodado

print('O preço a pagar será de R${}'.format((0.15*v1)+(60*v2)))