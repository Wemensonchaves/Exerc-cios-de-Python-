import random
from time import sleep
print('Sou seu computador...')
sleep(2)
print ('Acabei de pensar em um número entre 0 e 10. \n'
       '- A cada erro você perde um ponto \n'
       '- se você chegar a 0 pontos vc perde!')
sleep(2)
sorteio = random.randint(0,5)
sleep(2)
tentativa = 0
acertou = False
pontuação = 10
print ('Será que você consegue adivinhar qual foi..')
sleep(2)
nome = int(input('Escolha um número de 0 a 5: '))
while not nome == sorteio:
    tentativa += 1
    if nome > sorteio:
        nome = int(input('Errou! Tente um número menor!: '))
        print('Processando')
        sleep(1)
    elif nome < sorteio:
        nome = int(input('Errou! Tente um numero maior!: '))
        print('Processando')
        sleep(1)
    pontuação -= 2
    if tentativa >= 5:
        print(f'GAME OVER! o computador escolheu o número {sorteio}.')
    if tentativa >=0:
        print (f'Acertou! o computador escolheu o número {sorteio}')
    else:
        print(f'GAMER OVER! O computador escolheu o número {sorteio}!')
'''while not acertou:
    escolha = int(input('Qual é o seu palpite?'))
    tentativa += 1
    if escolha == sorteio:
        acertou = True
    else:
        if sorteio < escolha:
            print("Menos... tente mais uma vez")
        else:
            print('mais... tente mais uma vez.')
while sorteio != escolha:
    tentativa += 1
    if sorteio > escolha:
        escolha = int(input('Mais... Tente mais uma vez.'))
    else:
        escolha = int(input('Menos... Tente mais uma vez.'))
print (f'Acertou com {tentativa} tentativas. Parabéns.')'''