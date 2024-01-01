tot1000 = total = menor = cont = 0
barato = ' '
while True:
    print('----'*5)
    print('LOJA SUPER BARATO')
    print('----'*5)
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    opção = ' '
    while opção not in "SN":
         opção = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if preço >= 1000:
        tot1000 += 1
    if cont ==1 or preço <menor:
        menor = preço
        barato = produto
    total += preço
    if opção == 'N':
        break
print('{:-^45}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {total:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')