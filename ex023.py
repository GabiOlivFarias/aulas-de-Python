num= int(input('Digite um numero, de 0 a 9999: '))
u = num//1 %10
d = num//10 %10
c = num//100 %10
m = num //1000 %10
print('Analizando o numero {}'.format(num))
print('esse numero tem {} unidades'.format(u))
print('esse numero tem {:.0f} Dezenas'.format(d))
print('esse numero tem {:.0f} Centenas'.format(c))
print('esse numero tem {:.0f} unidades de milhar'.format(m))