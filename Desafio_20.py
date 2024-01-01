import random

n1 = str (input('primeiro aluno'))
n2 = str (input('segundo aluno'))
n3 = str (input('terceiro aluno'))
n4 = str (input('quarto aluno'))
li = [n1,n2,n3,n4]
#random.shuffle(li)
#random.sample(li,k = 2)
print(f'A ordem de apresentação será {random.sample(li,k=2)}')