print('Digite seu peso Kg: ',end='')
peso = float(input())

print('Digite sua altura cm: ',end='')
altura = int(input())/100

imc = peso / (altura**2)

if imc < 18.5:
    print('Imc: {:.1f}'.format(imc))
    print('Abaixo do peso!')
    
elif imc >= 18.5 and imc < 25: 
    print('Imc: {:.1f}'.format(imc))
    print('Peso ideal')

elif imc >= 25 and imc < 30:
    print('Imc: {:.1f}'.format(imc))
    print('Sobrepeso')

elif imc >= 30 and imc < 40:
    print('Imc: {:.1f}'.format(imc))
    print('Obesidade')

else:
    print('Imc: {:.1f}'.format(imc))
    print('Obesidade mórbida')

# O Programa de Cálculo de Índice de Massa Corporal (IMC) em Python
# é uma aplicação concebida para determinar o IMC com base no peso e
# altura fornecidos pelo usuário. O programa solicita que o usuário insira
# seu peso em quilogramas e altura em centímetros, realiza os cálculos
# necessários e categoriza o resultado conforme as faixas estabelecidas
# pela Organização Mundial da Saúde (OMS).
 
    
# The Body Mass Index (BMI) Calculation Program in Python is an application
# designed to determine the BMI based on the weight and height provided by
# the user. The program prompts the user to input their weight in kilograms
# and height in centimeters, performs the necessary calculations, and categorizes
# the result according to the ranges established by the World Health Organization (WHO).