#Minha resolução
'''aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
print('-=-'*15)
print(f"- Nome é igual a {aluno['nome']}")
print(f"- A média é igual a {aluno['media']}")
if aluno['media'] > 7.0:
    print('- situação é igual a aprovado')
elif aluno['media'] < 7.0 and aluno['media'] >= 5.0:
    print('- situação é igual a recuperação')
else:
    print('- situação é igual a reprovado')
print(aluno)'''

#Resolução Guanabara
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'    -{k} é igual a {v}')