import pygame
import os
import cnfig

pygame.mixer.init()

#temporal------------------------
africa = pygame.mixer.Sound(os.path.join(cnfig.sfx_folder, 'africa.wav'))

pygame.mixer.music.load(os.path.join(cnfig.sfx_folder, 'test.ogg'))
#--------------------------------
