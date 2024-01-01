'''print('====='*7)
print('{:^30}'.format('BANCO CEV'))
print('====='*7)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd == 20
        elif céd == 20:
            céd == 10
        elif céd == 10:
            céd == 1
        totcéd == 0
        if total == 0:
            break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''

'''valor = int(input("Informe o valor a ser sacado: "))
nota50 = valor//50
valor %= 50
nota20 = valor//20
valor %= 20
nota10 = valor//10
valor %= 10
nota1 = valor//1
print(f'Notas de 50 = {nota50}')
print(f"Notas de 20 = {nota20}")
print(f"Notas de 10 = {nota10}")
print(f"Notas de 1 = {nota1}")'''

print(\033[33m-=-'*21')