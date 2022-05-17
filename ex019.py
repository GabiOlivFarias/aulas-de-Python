import random
n1 = str(input('Primeiro aluno: ')) #aqui eu coloco os nomes
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4] #aqui ele guarda os nomes na lista
sort = random.choice(lista) #aqui ele vai escolha -randint- da lista
print('O escolhido foi {}'.format(sort))