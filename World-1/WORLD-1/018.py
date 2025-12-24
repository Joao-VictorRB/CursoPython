from math import sin,cos,tan,radians

print('Digite o valor de um ângulo: ',end='')
v=float(input())
v2=radians(v)
print('Ângulo:{}\nseno:{:.2f}\ncosseno:{:.2f}\ntangente:{:.2f}'.format(v,sin(v2),cos(v2),tan(v2)))