print('Digite seu nome completo: ',end='')
v=str(input(''))

v = v.strip()
upper = v.upper()
lower = v.lower()
NoSpace = (len(v)) - (v.count(' '))
Pn = (v.split()) 
Pn2 = len(Pn[0])

print('='*20)

print('''Nome maiúsculo:{}
Nome minúsculo:{}
Quantas letras sem espaço:{} 
Quantas letras tem o primeiro nome:{}'''.format(upper,lower,NoSpace,Pn2))