medidade = 0
cont = 0
pessoas = int(input("Quantas pessoas você quer cadastrar? "))
for p in range(1,2):
    print(f'----- {p}° PESSOA -----')
    nome = str(input('Nome: ')).lower().strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).upper()
    medidade += medidade
    cont += 1
media = float(medidade)
print(cont)
print(f'A média de idade do grupo {media:.2f} anos')