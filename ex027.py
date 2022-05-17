nome = str(input('Digite seu nome completo: ')).strip()
Pnome=nome.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(Pnome[0]))
print('Seu ultimo nome é {}'.format(Pnome[len(Pnome)-1]))
#acima contei quantos indices foi dividio no len e mostrei de tras p frente c -1