nome = str (input('Qual o seu nome:?')).strip()
print (f'Seu nome em maiúsculo é {nome.upper()}')
print (f'Seu nome em minúscula é {nome.lower()}')
print ('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
#print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print ('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

'''print (nome.upper()) #maiúscula
print (nome.lower())  #minusculo
print (nome.lower().capitalize()) #primeira letra maiúscula
print (nome.title()) #Cada palavra da String maiúscula
print (nome.islower()) #Ver se a string dada é totalmente maiúscula
print (len (nome))
print (nome.count('jose'))'''