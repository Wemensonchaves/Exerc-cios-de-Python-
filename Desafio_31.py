distancia = float(input('Qual é a distância da sua viagem?'))
print (f'Você está prestes a começar uma viagem de {distancia} km')
'''if distancia <= 200:
    preco = distancia*0.50
else:
    preco = distancia*0.45'''
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.56
print (f'E o preço da sua passagem R${preco:.2f}')