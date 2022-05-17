nome= str(input('Digite seu nome completo: ')).strip()#ja eliminando os espaços, antes e depois
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem o total de {} letras'.format(len(nome)- nome.count(' ')))
#print('Seu Primeiro nome é {} e ele tem {} letras'.format(,nome.find(' ')))
#acima achou onde ta o primeiro espaço e colocou contando o 1 nome
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
