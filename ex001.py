def c(): #defini uma função c()
    global canal #aqui disse que a var é global assim posso chamar fora da função def
    canal = 'gabriela' #acima primeiro eu chamo ela e depois na linha de baixo a declaro

#acima deixei indentado e deu erro, cuidado p não indentar
c()
print(canal)

