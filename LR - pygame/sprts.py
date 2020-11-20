#use spritesheets to set images

import pygame       #motor
import os           #folder management
import cnfig        #configuration variables

def find_index(L,item):
    try: index = L.index(item)
    except ValueError: index = 10
    return index

class Topview_player(pygame.sprite.Sprite):

    def __init__(self,image,size,pos):

        pygame.sprite.Sprite.__init__(self)

        scale = 1280.0 / cnfig.screen_size[0]

        size_x = size[0] * scale
        size_y = size[1] * scale
        self.size = int(size_x), int(size_y)                          #size of the sprite

        image = pygame.image.load(os.path.join(cnfig.img_folder,image))
        image = pygame.transform.scale(image,self.size)    #image

        self.rect = image.get_rect()                   #hit-box

        self.image = pygame.Surface((self.rect.right-self.rect.left,self.rect.bottom-self.rect.top))
        self.image.fill((cnfig.bg_color))
        self.image.blit(image,(0,0))

        pos_x = pos[0] * scale
        pos_y = pos[1] * scale
        self.rect.topleft = int(pos_x), int(pos_y)                    #position of top-left

        self.last_update = 0                                #animation update register
        self.facing = [None]                                #artificial pseudo-stack for actual facing
        self.last_facing = 'down'                           #str, last facing before going to [None]
        self.on_animation = 0                               #0->walk1; 1->walk2

    def update(self):

        if cnfig.new_screen_size != cnfig.screen_size:

            size = self.size
            pos = self.rect.topleft
            scale = float(cnfig.new_screen_size[0]) / cnfig.screen_size[0]

            size_x = size[0] * scale
            size_y = size[1] * scale
            self.size = int(size_x), int(size_y)                          #size of the sprite

            self.image = pygame.transform.scale(self.image,self.size)    #image

            self.rect = self.image.get_rect()                   #hit-box

            pos_x = pos[0] * scale
            pos_y = pos[1] * scale
            self.rect.topleft = int(pos_x), int(pos_y)                    #position of top-left

            cnfig.walk_step = int(cnfig.walk_step * scale)

        #if player is over half the screen and a little bit more, move everything in the opposite direction to simulate a "camera"
        if self.rect.centerx > cnfig.screen_size[0] / 2 + 20 * cnfig.walk_step:
            cnfig.camera_move = (cnfig.walk_step, cnfig.camera_move[1])
        elif self.rect.centerx < cnfig.map_size[0] - (cnfig.screen_size[0] / 2) - 20 * cnfig.walk_step:
            cnfig.camera_move = (-cnfig.walk_step, cnfig.camera_move[1])
        if self.rect.centery > cnfig.screen_size[1] / 2 + 20 * cnfig.walk_step:
            cnfig.camera_move = (cnfig.camera_move[0], cnfig.walk_step)
        elif self.rect.centery < cnfig.map_size[1] - (cnfig.screen_size[1] / 2) - 20 * cnfig.walk_step:
            cnfig.camera_move = (cnfig.camera_move[0], -cnfig.walk_step)

        keys = pygame.key.get_pressed()

        #move around with arrow keys
        #if two opposite keys pressed at the same time, only execute the latest one
        if cnfig.can_move:

            if keys[pygame.K_LEFT] and find_index(self.facing,'right') > find_index(self.facing,'left'):
                self.rect.left -= cnfig.walk_step
                collisions = pygame.sprite.spritecollide(topview_player,solid_group,False)
                if collisions:
                    self.rect.left += cnfig.walk_step

            if keys[pygame.K_RIGHT] and find_index(self.facing,'right') < find_index(self.facing,'left'):
                self.rect.left += cnfig.walk_step
                collisions = pygame.sprite.spritecollide(topview_player,solid_group,False)
                if collisions:
                    self.rect.left -= cnfig.walk_step

            if keys[pygame.K_UP] and find_index(self.facing,'down') > find_index(self.facing,'up'):
                self.rect.top -= cnfig.walk_step
                collisions = pygame.sprite.spritecollide(topview_player,solid_group,False)
                if collisions:
                    self.rect.top += cnfig.walk_step

            if keys[pygame.K_DOWN] and find_index(self.facing,'down') < find_index(self.facing,'up'):
                self.rect.top += cnfig.walk_step
                collisions = pygame.sprite.spritecollide(topview_player,solid_group,False)
                if collisions:
                    self.rect.top -= cnfig.walk_step

        self.rect.left -= cnfig.camera_move[0]
        self.rect.top -= cnfig.camera_move[1]

        self.walk_animation()

    def walk_animation(self):

        now = pygame.time.get_ticks()

        if now - self.last_update > 15:

            if self.facing[0] != None:

                self.last_facing = self.facing[0]

                #first walking frame
                if self.on_animation <= 9:

                    if self.facing[0] == 'down':
                        self.change_image('player_4.png')
                    elif self.facing[0] == 'up':
                        self.change_image('player_5.png')
                    elif self.facing[0] == 'left':
                        self.change_image('player_6.png')
                    elif self.facing[0] == 'right':
                        self.change_image('player_7.png')

                #second walking frame
                elif self.on_animation > 9:

                    if self.facing[0] == 'down':
                        self.change_image('player_8.png')
                    elif self.facing[0] == 'up':
                        self.change_image('player_9.png')
                    elif self.facing[0] == 'left':
                        self.change_image('player_10.png')
                    elif self.facing[0] == 'right':
                        self.change_image('player_11.png')

                self.last_update = now
                self.on_animation += 1
                self.on_animation %= 20

            else:

                #standing frame
                if self.last_facing == 'down':
                    self.change_image('player_0.png')
                elif self.last_facing == 'up':
                    self.change_image('player_3.png')
                elif self.last_facing == 'left':
                    self.change_image('player_1.png')
                elif self.last_facing == 'right':
                    self.change_image('player_2.png')

    def change_image(self,image):

        image = pygame.image.load(os.path.join(cnfig.img_folder,image))
        image = pygame.transform.scale(image,self.size)    #image

        pos = self.rect.topleft

        self.rect = image.get_rect()                   #hit-box

        self.image = pygame.Surface((self.rect.right-self.rect.left,self.rect.bottom-self.rect.top))
        self.image.fill((cnfig.bg_color))
        self.image.blit(image,(0,0))

        self.rect.topleft = pos

        self.setup(self.group)

    def setup(self,group):

        self.image = self.image.convert()
        self.image.set_colorkey((cnfig.bg_color))
        group.add(self)
        self.group = group

class Map_sprite(pygame.sprite.Sprite):

    def __init__(self,image,size,pos):

        pygame.sprite.Sprite.__init__(self)

        scale = 1280.0 / cnfig.screen_size[0]

        size_x = size[0] * scale
        size_y = size[1] * scale
        self.size = int(size_x), int(size_y)                         #size of the sprite

        image = pygame.image.load(os.path.join(cnfig.img_folder,image))
        image = pygame.transform.scale(image,self.size)    #image

        self.rect = image.get_rect()                   #hit-box

        self.image = pygame.Surface((self.rect.right-self.rect.left,self.rect.bottom-self.rect.top))
        self.image.fill((cnfig.bg_color))
        self.image.blit(image,(0,0))

        pos_x = pos[0] * scale
        pos_y = pos[1] * scale
        self.rect.topleft = int(pos_x), int(pos_y)                    #position of top-left

    def update(self):

        if cnfig.new_screen_size != cnfig.screen_size:

            size = self.size
            pos = self.rect.topleft
            scale = float(cnfig.new_screen_size[0]) / cnfig.screen_size[0]

            size_x = size[0] * scale
            size_y = size[1] * scale
            self.size = int(size_x), int(size_y)                          #size of the sprite

            self.image = pygame.transform.scale(self.image,self.size)    #image

            self.rect = self.image.get_rect()                   #hit-box

            pos_x = pos[0] * scale
            pos_y = pos[1] * scale
            self.rect.topleft = int(pos_x), int(pos_y)                    #position of top-left

        self.rect.left -= cnfig.camera_move[0]
        self.rect.top -= cnfig.camera_move[1]

    def setup(self,group):

        self.image = self.image.convert()
        self.image.set_colorkey((cnfig.bg_color))
        group.add(self)

bottom_passthrough_group = pygame.sprite.Group()
top_passthrough_group = pygame.sprite.Group()
solid_group = pygame.sprite.Group()
menu_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

logo_reteam = Map_sprite(image='reteam_logo.png',size=(1280,720),pos=(0,0))

def create_sprites():

    global topview_player
    global example_tile_0
    global example_tile_1
    global example_tile_2
    global map_main_city

    topview_player = Topview_player(image='player_0.png',size=cnfig.regular_sprite_size,pos=(620,340))

    #temporal---------------------
    example_tile_0 = Map_sprite(image='ground_0.png',size=cnfig.regular_sprite_size,pos=(128,256))
    map_main_city = Map_sprite(image='map_main_city.png',size=(2*2640,2*2760),pos=(-640,-600))
    example_tile_1 = Map_sprite(image='sign_0.png',size=cnfig.regular_sprite_size,pos=(256,64))
    example_tile_2 = Map_sprite(image='sign_1.png',size=cnfig.regular_sprite_size,pos=(256,128))
    #-----------------------------
