from termcolor import colored
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print (f'Tirando {n1} e {n2} a média do aluno é {media}')
if media >= 6.0:
    print ('Aluno está \033[0;33mAPROVADO ')
elif media <6.0 and media >3.0:
    print ('Aluno não foi aprovado mais tem direitro a uma PROVA DE RECUPERAÇÃO')
    rec = float(input('''Aluno fez a prova de recuperação:
     [1] Sim
     [2] Não
     Opção escolhida: '''))
    if rec == 1:
        novanota = float(input('Qual a foi a nota obtida na prova de recuperação:'))
        if novanota > 6.0:
            print(f'Aluno obtive na prova de recuperação a nota {novanota} e foi APROVADO')
        else:
            print(f'Aluno obtive na prova de recuperação a nota {novanota} e foi REPROVADO')
else:
    print ('Aluno REPROVADO')