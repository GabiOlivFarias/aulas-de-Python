tc = float(input('digite a temperatura em ºC: '))
tf = tc*1.8+32
tk = tc+232.15
print('a temperatura de {}ºC equivale a {} Fahrenheit'.format(tc, tf),end=' ')
print('ou a {} Kelvin'.format(tk))