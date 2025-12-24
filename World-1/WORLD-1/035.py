print('Primeiro segmento: ',end='')
r1=float(input())

print('Segundo segmento: ',end='')
r2=float(input())

print('Terceiro segmento: ',end='')
r3=float(input())

lista =[r1,r2,r3]
asc = sorted(lista)

maxi = asc [2]
med= asc [1]
min = asc [0]
soma = med + min

if soma >= maxi:
    print('Essas retas PODEM forma um triângulo')
else:
    print('Essas retas NÃO PODEM forma um triângulo')