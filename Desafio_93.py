dados = dict()
gol = list()
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas Zico jogou? '))
for i in range(partidas):
    gol.append(int(input(f'Quantos gols na partida {i}? ')))
dados['gols'] = gol
dados['total'] = sum(gol)
print('-=-'*25)
print(dados)
print('-=-'*25)
print(f'O campo nome tem o valor {dados["nome"]}')
print(f'O campo gols tem o valor {dados["gols"]}')
print(f'O campo total tem o valor {dados["total"]}')
print('-=-'*25)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for k,v in enumerate(dados["gols"]):
         print(f' => Na partida {k}, fez {v} gols. ')
print(f'Foi um total de {dados["total"]} partidas')


