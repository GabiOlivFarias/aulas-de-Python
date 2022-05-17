import emoji
import pygame
vel= float(input('Qual velocidade do automovel? km'))
if vel <= 80:
    print (emoji.emojize('Dirija em segurança! :automobile:', variant="emoji_type"))
else:
    print(emoji.emojize('Multado! você ultrapassou a velocidade permitida :oncoming_police_car:',variant="emoji_type"))
    print('Sua velocidade é de {} km/h e sua multa será de R${}'.format(vel, (vel-80)*7))
    pygame.init()
    pygame.mixer.music.load('vel.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
