import pygame
from pygame import mixer
#iniciando o mixer do pygame
mixer.init()
pygame.init()
mixer.music.load('de21.mp3')
mixer.music.play()
pygame.event.wait()
print ('Agora vcoê escuta?')
