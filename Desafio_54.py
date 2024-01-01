from datetime import date, datetime
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasceu = int (input(f'Em que ano {pess}° a pessoa nasceu'))
    idade = atual - nasceu
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print (f'Ao todos tivemos {totmaior} pessoas maiores de idade')
print (f'Ao todos tivemos {totmenor} pessoas menores de idade')
