import random
import emoji
import pygame
from time import sleep
print('-=-'*30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*30)
num= int(input('Em que numero eu pensei?'))
numran= random.randint(0,5)
print('Processando...')
sleep(3)
if num == numran:
    print(emoji.emojize("Acertô misaravi! :call_me_hand:", variant="emoji_type"))

else:
    print(emoji.emojize("Tente outra vez! :confused_face:", variant="emoji_type"))
    print('eu pensei no numero {}'.format(numran))
    pygame.init()
    pygame.mixer.music.load('raul.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
