from random import randint
v = 0
while True:
    print("=-=-" * 7)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-=-' * 7)
    valor = int(input('Diga um valor: '))
    aposta = ' '
    while aposta not in 'PI':
        aposta = str(input('Par ou Ímpar [P/I]')).strip().upper()[0]
    computador = randint(0,9)
    soma = (valor + computador)
    print(f'Você jogou {valor} e o computador {computador}. Totalizou {valor + computador}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if aposta == 'P':
        if soma % 2 == 0:
            print ('Você VENCEU!')
            v += 1
        else:
            print ('Você PERDEU')
            break
    elif aposta == 'I':
        if soma % 2 == 1:
            print ('Você VENCEU')
            v += 1
        else:
            print ('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {v} vezes.')