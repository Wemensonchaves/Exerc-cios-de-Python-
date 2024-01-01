print('LOJAS CHAVÉS')
preco = float (input('Preço das compras R$: '))
print('''FORMAS DE PAGAMENTOS
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção:'))
if opção == 1:
    total = preco - (preco*0.10)
elif opção == 2:
    total = preco - (preco*0.05)
    print (f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final')
elif opção ==3:
    total = preco/2
    print(f'Sua compra de R${preco:.2f} será parcelada em 2x R${total:.2f} no final')
elif opção == 4:
    total = preco + (preco*0.20)
    totpar = int(input('Quantas parcelas?'))
    parcela = total/totpar
    print (f"Sua compra será parcelada em {totpar}x de R$ {parcela:.2f} COM JURO")
print(f'Sua compra de R${preco:.2f} vai custa R${total} no final')