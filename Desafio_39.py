from datetime import date
sexo = int (input('''Informe seu sexo:
[1] Masculino
[2] Feminino
opção: '''))
if sexo == 2:
    print ("Você não precisa se alistar")
elif sexo == 1:
    ano = int(input("Seu ano de nascimento:"))
    atual = date.today().year
    idade = atual - ano
    print (f'Quem nasceu em {ano} tem {idade} anos em 2020')
    if 18 < idade:
        print (f'Você já deveria ter se alistado há {idade-18} anos')
    elif idade == 18:
        print ('Você deve-se alistar imediatamente')
    else:
        print ("Você ainda não tem 18 anos")
else:
    print ('Opção escolhida incorreta. Tente novamente')



