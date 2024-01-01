from random import randint
from time import sleep 
from termcolor import colored
print (colored('-=-', 'yellow')*19)
print ('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print (colored('-=-', 'yellow')*19)
n = int(input('Que número eu pensei?'))
p = randint(0,5)
print('Processando...')
if n == p:
    print (colored(f'Perdi! Você acerto, pensei no número {p} e você também pensou no número {n}', 'red'))
else:
    print (colored (f'Ganhei! Eu pensei no número {p} e não no {n}!', 'green'))
print ('Fim')