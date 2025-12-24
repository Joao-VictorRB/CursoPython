print('Digite o preço do produto: ',end='')
v= float(input())

print('O produtor com 5% de desconto valerá R${:.2f}'.format(v-(5*v)/100))