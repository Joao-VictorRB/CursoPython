print('Qual a velocidade do carro em km: ',end='')
v=int(input())

if v > 80:
    multa = (v-80)*7
    
    print('Você foi multado em R${}'.format(multa))

else:
    print('Você esta dentro do limite permitido')