#improve text management

import pygame
import cnfig

pygame.font.init()
font_arial = pygame.font.match_font('arial')

class Text(pygame.sprite.Sprite):

    def __init__(self,text,size,pos,font=font_arial,color=(255,255,255),txt_type='default'):

        pygame.sprite.Sprite.__init__(self)

        self.size = size * 1280 / cnfig.screen_size[0]
        self.font_name = font
        self.font = pygame.font.Font(self.font_name,self.size)
        self.text = text
        self.color = color
        self.type = txt_type
        self.pos = pos

        if self.type == 'chat':
            image = self.font.render(self.text[0], True, self.color)
            self.index = 0
            self.counter = 0

        elif self.type == 'default':
            image = self.font.render(self.text, True, self.color)

        self.rect = image.get_rect()                   #hit-box

        self.image = pygame.Surface((self.rect.right-self.rect.left,self.rect.bottom-self.rect.top))
        self.image.fill((cnfig.bg_color))
        self.image.blit(image,(0,0))

        self.rect.topleft = self.pos

    def update(self):

        if cnfig.new_screen_size != cnfig.screen_size:

            scale = float(cnfig.new_screen_size[0]) / cnfig.screen_size[0]

            self.size = int(self.size * scale)
            self.font = pygame.font.Font(self.font_name,self.size)

            pos_x = self.pos[0] * scale
            pos_y = self.pos[1] * scale
            self.pos = int(pos_x), int(pos_y)

            if self.type == 'default':

                image = self.font.render(self.text, True, self.color)

                self.rect = image.get_rect()                   #hit-box

                self.image = pygame.Surface((self.rect.right-self.rect.left,self.rect.bottom-self.rect.top))
                self.image.fill((cnfig.bg_color))
                self.image.blit(image,(0,0))

                self.rect.topleft = self.pos

                self.setup(self.group)

        if self.type == 'chat':

            if self.index <= len(self.text) and self.counter == cnfig.text_speed:

                image = self.font.render(self.text[0:self.index+1], True, self.color)

                self.rect = image.get_rect()                   #hit-box

                self.image = pygame.Surface((self.rect.right-self.rect.left,self.rect.bottom-self.rect.top))
                self.image.fill((cnfig.bg_color))
                self.image.blit(image,(0,0))

                self.rect.topleft = self.pos

                self.index += 1
                self.setup(self.group)
                self.counter = 0

            self.counter += 1

            if self.index == len(self.text): self.type = 'default'

    def setup(self,group):

        self.image = self.image.convert()
        self.image.set_colorkey((cnfig.bg_color))
        group.add(self)
        self.group = group

#temporal-------------------------
text_0 = "Hi!, I'm Mei, just the average highschool student running late with bread in her mouth"
chat_box = Text(text_0,16,(128,550),txt_type='chat')
#---------------------------------
