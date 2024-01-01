tot18 = toth = totm20 =  0
while True:
    print('----'*5)
    print('CADASTRE UMA PESSOA')
    print('----'*5)
    idade = int(input('Idade: '))
    sexo = " "
    while sexo not in 'MF':
        sexo = str(input('Sexo: [Mm/Ff] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    print ('----'*5)
    resp = " "
    while resp not in 'SN':
         resp = str(input('Quer continuar? [Ss/Nn] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totm20} mulheres com menos de 20 anos')

