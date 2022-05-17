n = int(input('Digite um numero: '))
es= int(input('''\033[1:33m Escolha qual base de conversão: \033[m
      [1] Binário;
      [2] Octal;
      [3] Hexadecimal:'''))
if es==1:
    n%2
    print('você escolheu a conversão para \033[1:32m binário')
    print('O número {} convertido para binário é {}'.format(n, ))
