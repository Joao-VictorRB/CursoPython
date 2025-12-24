print('Primeiro segmento: ',end='')
r1=float(input())

print('Segundo segmento: ',end='')
r2=float(input())

print('Terceiro segmento: ',end='')
r3=float(input())

if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('Essas retas PODEM forma um triângulo',end='')
    
    if r1 == r2 and r2 == r3:
     print(' QUILÁTERO')

    elif r1 == r2 or r1 == r3 or r2 == r3:
     print(' ISÓSCELES')

    elif r1 != r2 and r1 != r3 and r2 != r3:
     print(' ESCALENO')
    
else:
    print('Essas retas NÃO PODEM forma um triângulo')
    

# O Programa de Classificação de Triângulos em Python foi projetado para determinar
# e classificar um triângulo com base nos comprimentos de seus três lados, fornecidos
# pelo usuário. O programa solicita que o usuário insira os comprimentos de três segmentos,
# realiza os cálculos necessários e, em seguida, classifica o triângulo em diferentes tipos,
# incluindo Equilátero, Isósceles ou Escaleno, seguindo o teorema da desigualdade de triângulos.
  
    
# The Triangle Classification Program in Python is designed to determine and classify a triangle based
# on the lengths of its three sides, provided by the user. The program prompts the user to input the
# lengths of three segments, performs the necessary calculations, and then classifies the triangle into
# different types, including Equilateral, Isosceles, or Scalene, following the triangle inequality theorem. 