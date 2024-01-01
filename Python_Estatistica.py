#Introdução à Numpy
import numpy

#Arrays
'''lista = [1,2,3,4,5]
x = numpy.array(lista)
print(lista)'''

'''x = numpy.array([1,2,3,4,5])
y = 2

print(x+y)
print(x-y)
print(y-x)
print(x*y)
print(x/y)
print(y/x)'''

'''x = numpy.array([1,2,3,4,5])
y = numpy.array([6,7,8,9,10])

print(x+y)
print(x-y)
print(y-x)
print(x*y)
print(x/y)
print(y/x)'''

#numpy.sun(x) : retorna a soma de todos os elementos de x
#numpy.max(x) : retorna o valor máximo contido em x
#numpy.min(x) : retorna o valor mínimo  contido em x

# gerando um array com 100 valores aleatorios
# sorteados entre 0 e 100
x = numpy.random.randint(low = 0, high = 1000, size = 100) # low = começo; high = final (intervalo) e size = quantidade números sorteados

'''print(x)'''

#Calculando a media utilizando os metodos
#numpy.sum e len

'''media = numpy.sum(x) / len(x)
print(media)'''

#Mediana
mediana = numpy.median(x)
print(mediana)

#Percentis
percentil_15 = numpy.percentile(x,15)
print(percentil_15)

#Amplitude

valor_máximo = numpy.max(x)
valor_mínimo = numpy.min(x)
intervalor = valor_máximo - valor_mínimo
print(intervalor)

#Variância e desvio padrão
media = numpy.mean(x)
n = len(x)
diferença = x - media
variancia = numpy.sum(diferença * diferença) / (n - 1)
desvio_padrão = numpy.sqrt(variancia)
print(desvio_padrão)

## de maneira mais facil, podemos utilizar as seguintes funções

variancia = numpy.var(x, ddof= 1) #ddof indica o número de graus de liberdade utilizados.
desvio_padrão = numpy.std(x, ddof= 1)
print(desvio_padrão)

#Medidas de distribuição
#Obliquidade

import numpy
import scipy.stats
# gerando uma amostra com 10000 observacoes a partir de
# uma distribuicao normal com media zero e desvio-padrao
# unitario
dados = numpy.random.normal(loc=0.0, scale=1.0, size=10000)
# como os dados foram gerados segundo uma distribuicao
# normal, que eh simetrica, a obliquidade devera resultar
# em algum valor proximo de 0
obliquidade = scipy.stats.skew(dados) #a obliquidade dos dados contidos em um array pode ser calculada por meio da biblioteca SciPy
print(obliquidade)


#curtose

import numpy
import scipy.stats
# gerando uma amostra com 10000 observacoes a partir de
# uma distribuicao normal com media zero e desvio-padrao
# unitario
dados = numpy.random.normal(loc=0.0, scale=1.0, size=10000)
# como os dados foram gerados segundo uma distribuicao
# normal, que eh simetrica, a curtose devera resultar
# em algum valor proximo de 0
curtose = scipy.stats.kurtosis(dados)
print(curtose)


#Dados multivariados
'''Para carregar o arquivo CSV para o conjunto de dados Iris, recomenda-se a utilização
da biblioteca Pandas, a qual dispõe do tipo de dados DataFrame, que tem uma
estrutura tabular, similar àquela apresentada na Tabela 2.1. Assim, pode-se proceder da
seguinte maneira:'''

#Visualização de dados
#Histogramas

#Caculando o histograma para uma variável


'''from matplotlib import pyplot

#Notas na primeira prova
notas = numpy.array([2,5,7,3,5,6,5,6,6,5,5,3])
print(notas)

pyplot.hist(notas, bins='auto') #Intervalo automático
pyplot.title('Histograma') #Titulo do gráfico
pyplot.ylabel('Frequencia') #Titulo do eixo horizontal/y
pyplot.xlabel('Nota') #Titulo do eixo vertical/x
pyplot.show()  #Mostrar o gráfico'''

#Scatter plots

#Gráfico comumente utilizado para observar o comportamento de duas variáveis de uma base de dados.

#Um scatter plot pode ser gerado por meio do seguinte código:

import pandas
from matplotlib import pyplot

#Carregando iris.csv
dados = pandas.read_csv('iris.csv')

#Criando um dicionário  para mapear cada classe para uma cor
classe_cor = {'Iris-setosa' : 'red',
              'Iris-virginica' : 'blue',
              'Iris-versicolor' : 'green'}

#Criando uma lista com as cores de cada exemplo
cores = [classe_cor[nome] for nome in dados.Name]

#Gerando scatter plot
# no eixo x sera plotado o tamanho da sepala
# no eixo y sera plotado o comprimento da sepala

#Box plot

from pandas.plotting import scatter_matrix #
from matplotlib import pyplot

#Carregando iris.csv
dados = pandas.read_csv('iris.csv')

#gerando um bloxplot para os atributos da Iris
dados.plot(kind='box')
pyplot.show()














