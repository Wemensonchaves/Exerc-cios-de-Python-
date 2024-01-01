peso = float (input('Qual o seu peso (Kg)?'))
altura = float (input('Qual sua altura (m)'))
imc = peso / (altura**2)
print (f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.0:
    print ('Indivíduo classificado com magreza')
elif 18.5 <= imc < 25:
    print ('Indivíduo classificado como normal')
elif 25 >= imc < 29.9:
    print ('Indivíduo classificado com sobrepeso com grau 0')
elif 30 >= imc < 39.9:
    print('Indivíduo classificado com obesidade de grau 1')
else:
    print ('Indivíduo classificado com obesidade de grau 2')