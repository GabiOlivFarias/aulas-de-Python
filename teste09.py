frase = 'Curso em Vídeo Python     '
#print (frase[3::2])
print (frase.upper().count('C'))
print(len(frase.strip())) #tamanho da frase
print(frase.replace('Python', 'css')) #considerar cada letra upper e lower
print('Curso' in frase) # True or False
print(frase.lower().find('python'))# aqui me mostra onde começou o 'python'
#print(frase.split()) # aqui criou uma lista/tupla
dividido= frase.split() # aqui a var dividido recebeu a frase em tupla
print(dividido[0]) #mostra o indice 0 da var, que é 'Curso'
print(dividido[2][3])#o indice 2 e a letra 3 desse indice: 'e'
#p textos longos print('''texto''') ou aspas duplas
print('''Lorem Ipsum é simplesmente um texto fictício da indústria tipográfica
 e de impressão. Lorem Ipsum tem sido o texto fictício padrão da indústria desde
  os anos 1500, quando um impressor desconhecido pegou uma cozinha de tipos e 
  embaralhou-a para fazer um livro de espécimes de tipos. Ele sobreviveu não 
  apenas cinco séculos, mas também o salto para a composição eletrônica, permanecendo
   essencialmente inalterado.''')