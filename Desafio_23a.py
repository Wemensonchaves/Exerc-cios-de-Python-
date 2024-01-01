n1 = int(input('Digite um npumero entre 0 e 9999 '))
n2 = str(int(n1)).zfill(4) #Preenche/coloca zero na frente do número digitado
print(f'O número {n1} possui, {n2[0]} milhares')
print(f'O número {n1} possui, {n2[1]} centenas')
print(f'O número {n1} possui, {n2[2]} dezenas')
print(f'O número {n1} possui, {n2[3]} unidades')