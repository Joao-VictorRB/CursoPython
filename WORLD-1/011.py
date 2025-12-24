print('Digite a largura da parede em metros: ',end='')
l= float(input())
print('Digite a altura da parede em metros: ',end='')
h=(float(input()))

#1L de tinta pinta 2 metros quadrado

print('Para pintar {:.3f}m2 será preciso {:.1f}L de tinta'.format(l*h, (l*h)/2))