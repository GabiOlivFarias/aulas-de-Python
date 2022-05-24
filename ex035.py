import emoji
print('=-=-'*15)
print(emoji.emojize('Analizando triangulos :red_triangle_pointed_up: :', variant="emoji_type"))
print('=-=-'*15)
a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado:'))
if a+b>c and a+c>b and b+c>a:
    print('Com os valores digitados \033[0;31m pode-se \033[m formar um triangulo!')
else:
    print('Com os valores digitados não se pode formar um triangulo!')