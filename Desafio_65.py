resp = 's'
media = soma = quant = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
media = soma / quant
print (f'Você digitou {quant} números e a média é {media}')
print (f'O maior valor foi {maior} e o menor foi {menor}')