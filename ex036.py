print('\033[36m =-'*20)
print('\033[31m Simulação de emprestimo ')
print('\033[36m =-'*20)
vc = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite sua renda mensal: R$'))
ano = int(input('Em quantos anos será o parcelamento? '))
pres = vc/(ano*12)
if pres > (sal*30/100):
    print('Emprestimo \033[1:31m negado!')
else:
    print('Emprestimo \033[1:32m aprovado!')
