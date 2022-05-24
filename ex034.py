sal= float(input('Digite o salário atual: R$'))
if sal <= 3000:
    print('Quem ganha R${}, agora ganhará R${}'.format(sal, sal+(sal*15/100)))
else:
    print('Quem ganha R${}, agora ganhará R${}'.format(sal, sal+(sal*10/100)))