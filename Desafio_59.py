from time import sleep
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print(' [1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
    opção = int(input('>>>>> Qual é a sua opção?'))
    if opção == 1:
        resultado = (p1 + p2)
        print(f'O resultados de {p1} + {p2} é {resultado}')
    elif opção == 2:
        resultado = (p1 * p2)
        print(f'O resultado de {p1} * {p2} é {resultado}')
    elif opção == 3:
        if p1 > p2:
            print (f'O número {p1} é maior que o número {p2}')
        if p1 < p2:
            print (f'O número {p2} é maior que o número {p1}')
        else:
            print (f'Os números {p1} e {p2}  são iguais')
    elif opção == 4:
        p1 = int(input('Primeiro valor: '))
        p2 = int(input('Segundo valor: '))
    else:
        print('opção inválida. Tente novamente')
    print('=-=-' * 5)
print('Fim do programa! volte novamente.')