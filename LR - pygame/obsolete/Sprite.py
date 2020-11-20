#Sprite:
#
#   file_names(list(str)): list of names for the images and animation
#   relative_pos(tuple(float)): image position in game screen units
#   relative_size(tuple(float)): image size in game screen units
#   sprite_type(str): 'static', 'menu', 'player'
#
#   img(list(pygame.image)): list of loaded images
#   pos(tuple(float)): image position in game screen units
#   size(tuple(float)): image size in game screen units
#   is_rendered(int): index of the loaded image, -1 if not loaded
#   sprite_type(str): 'static', 'menu', 'player'

class Sprite:

    def __init__(self,file_names,relative_pos,relative_size,sprite_type):

        import pygame
        
        loaded_list = []
        for name in file_names:
            loaded_list.append(pygame.image.load(name))
        
        self._img = loaded_list 
        self._pos = relative_pos
        self._size = relative_size
        self._is_rendered = -1
        self._sprite_type = sprite_type

    #render: load image on screen
    def render(self,screen,screen_size,offset=(0,0)):

        import pygame

        sprite_img = self._img[self._is_rendered]
        sprite_size = (int(self._size[0]*screen_size[0]),\
                       int(self._size[1]*screen_size[1]))
        sprite_img = pygame.transform.scale(sprite_img,sprite_size)

        sprite_position = (int((self._pos[0]-offset[0])*screen_size[0]),\
                           int((self._pos[1]-offset[1])*screen_size[1])) 

        screen.blit(sprite_img,sprite_position)

    #load_frame: choose the sprite frame to load
    def load_frame(self,index):
        self._is_rendered = index

    #unload_frame: stop rendering sprite
    def unload_frame(self):
        self._is_rendered = -1

    #frame_loaded: return the loaded frame
    def frame_loaded(self):
        return self._is_rendered

    #add_pos: sum amount to sprite position
    def add_pos(self,coord,amount):
        if coord == 'x': self._pos = (self._pos[0]+amount,self._pos[1])
        elif coord == 'y': self._pos = (self._pos[0],self._pos[1]+amount)

    #set_pos: set sprite to amount as position
    def set_pos(self,coord,amount):
        if coord == 'x': self._pos = (amount,self._pos[1])
        elif coord == 'y': self._pos = (self._pos[0],amount)

    #get_pos: return sprite position
    def get_pos(self,coord,offset=(0,0)):
        if coord == 'x': return self._pos[0]+offset[0]
        elif coord == 'y': return self._pos[1]+offset[1]

    #get_size: return sprite size
    def get_size(self,coord):
        if coord == 'x': return self._size[0]
        elif coord == 'y': return self._size[1]
