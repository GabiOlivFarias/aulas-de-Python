'''catop = float(input('digite o tamanho em cm do cateto oposto: cm'))
catad = float(input('digite o tamanho em cm do cateto adjacente: cm'))
hip= (catop**2 + catad**2) ** (1/2)
print('como dizia Mamonas assassinas "a soma do quadrado dos catetos é ',end='')
print('igual a porra da hiponetusa..."')
print('nesse caso a hipotenusa vale: {:.2f}cm'.format(hip))'''
from math import hypot
catop = float(input('digite o tamanho em cm do cateto oposto: cm'))
catad = float(input('digite o tamanho em cm do cateto adjacente: cm'))
hip = hypot(catop,catad)
print('nesse caso a hipotenusa vale: {:.2f}cm'.format(hip))