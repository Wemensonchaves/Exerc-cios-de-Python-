casa = float(input('Qual o valor da casa R$?'))
sal = float(input('Salário do comprador: R$'))
ano = int(input ('Quantos anos de financiamento?'))
prest = float ((casa*1.30)/(ano*12))
print (f'Para pegar uma casa de R$ {casa:.2f} em {ano} anos', end='')
print (f' a prestação será de R$ {prest:.2f}')
if sal*0.30 >= prest:
    print('Empréstimo foi CONCEDIDO')
else:
    print('Empréstimo NEGADO')