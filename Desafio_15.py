dias = int(input('Quantos dias foram percorridos?'))
km = float (input('Quantos quilômetros foram percorridos?'))
valor = (dias*60)+(km*0.15)
print(f'O total a pagar é de R${valor:.2f}')