from termcolor import colored
print (colored('=-=', 'yellow')*8)
print ('ANALISADOR DE TRIÂNGULOS')
print (colored('=-=', 'yellow')*8)
a = float (input('Primeiro segmento:'))
b = float (input('Segundo segmento:'))
c = float (input('Terceiro segmento:'))
if ((b-c)<a<b+c) and ((a-c)<b<a+c) and ((a-b)<c<a+b):
    print ('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print ('Os segmentos acima NÃO PODEM FORMAR um triângulo')
