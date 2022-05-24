#import math ou
from math import sin, cos, tan, radians
ang = float(input('digite um angulo: '))
sen =  sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print('o ângulo digitado foi {:.2f}'.format(ang))
print('e seu seno é {:.2f}, cosseno é {:.2f} e tangente é{:.2f}'.format(sen, cos, tang))
