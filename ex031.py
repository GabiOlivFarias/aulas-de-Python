d = float(input('Digite a distancia percorrido: km'))
print('A distancia percorrida é de {} km'.format(d))
if d<= 200:
    print('O valor da passagem será de R${:.2f}'.format(d*0.50))
else:
    print('Ovalor da passagem será de R${:.2f}'.format(d*0.45))