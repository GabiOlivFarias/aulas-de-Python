d = float(input('digite uma distancia em metros: '))
print ('a medida em metros é igual a {:.3}m corresponde a:'.format(d))
#km/1000 hm/100 dam/10 m
#dm*10 cm*100 mm*1000
print('{}km ou {}hm ou {}dam'.format((d/1000), (d/100),(d/10),))
print('ou {}dm ou {}cm ou {}mm'.format((d*10), (d*100), (d*1000)))