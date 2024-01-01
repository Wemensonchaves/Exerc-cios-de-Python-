from time import sleep
from playsound import playsound
con= int(input('Qual deverá ser a contagem regressiva? '))
for c in range(con, -1, -1):
    print(c)
    sleep(0.25)
print('') #Pula uma linha
print('BUM! BUM! POOOW!')