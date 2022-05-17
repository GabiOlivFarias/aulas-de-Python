b = float(input('digite a largura da parede em metros: M'))
h = float(input('digite a altura da parede em metros: M'))
area = b*h
print('Sua parede tem dimensão de {}X{} e sua area é de {}m².'.format(b, h, area))
print('para pintar essa parede voce precisará de {:.2f} litros de tinta.'.format(area/2))
#print('ou seja {} latas de tinta.')