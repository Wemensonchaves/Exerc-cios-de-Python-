from math import hypot
co = float (input('Comprimento do cateto oposto:'))
ca = float (input('Comprimento do cateto adjacente:'))
#hi = hypot(co,ca)
#hi = (co**2+ca**2)**(1/2)
print (f'A hipotenuza vai medir {hypot(co,ca):.2f}')