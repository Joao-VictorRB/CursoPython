from datetime import date
import time

print('Qual o ano que você nasceu: ',end='')
ano_nasc =int(input())

data = date.today().year

data_alistamento = data-ano_nasc

print('calculando...') 
time.sleep(2)

if data_alistamento == 18:
   print('\033[1;32m Você está na idade de se alistar\033[m')

elif data_alistamento >= 18:
   print('\033[1;31m Você já passou do tempo de se alistar. Seu alistamento já passou há {} ano(s)\033[m'.format(data_alistamento-18))
   
else:
   print('\033[1;33mVocê ainda não idade suficiente para servi, Falta-lhe {} ano(s).\033[m'.format(18-data_alistamento))


# O Programa de Alistamento Militar Automatizado é uma aplicação desenvolvida em Python
# que permite determinar o status do alistamento militar de um indivíduo com base no seu
# ano de nascimento. Utilizando a biblioteca 'datetime', o programa obtém o ano atual da máquina
# em que está sendo executado, garantindo sua funcionalidade independente do ano.


# The Automated Military Enrollment Program is an application developed in Python that enables the
# determination of an individual's military enlistment status based on their year of birth. Utilizing
# the 'datetime' library, the program retrieves the current year from the machine on which it is being
# executed, ensuring its functionality independent of the specific year.