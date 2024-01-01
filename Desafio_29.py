'''from termcolor import colored
v = float (input('Qual é a velocidade atual do carro?'))
if v > 80:
    print (colored(f'MULTADO! você excedeu o limite permitido que é de 80 Km/h','red'))
    multa = (v-80)*7
    print (colored(f'Você deve pagar uma multa de R${multa:.2f}'))
print (colored('Tenha um bom dia! dirija com segurança','green'))'''
from termcolor import colored
from random import randint
from time import sleep
print ('Seu carro passou no radar....')
sleep(2)
vel = randint(10,120)
multa = ((vel-80)*7)
if vel > 80:
    print (f'Você estava a {vel}km e foi multado, o valor da multa é R${multa}')
else:
    print (f'Sua velocidade é {vel}km, continue respeitando os limites')