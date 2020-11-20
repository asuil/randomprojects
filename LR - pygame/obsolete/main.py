import pygame #pygame motor
from pygame.locals import * #keys
from sprites import * #sprites & Sprite class
from game_properties import * #propties & GameProperties class

class App:

    def __init__(self):

        self._running = True
        self._gamescreen = None
        self.size = self.weight, self.height = propties.screen_size

    def on_init(self):
        global player_sprites
        global static_sprites_bottom

        pygame.init()
        pygame.display.set_caption('Last Raindrops')
        self._gamescreen = pygame.display.set_mode(self.size)

        #sprite loading test----------------------
        static_sprites_bottom = lol_haha
        player_sprites = [topview_player]

        for sprite in static_sprites_bottom:
            sprite.load_frame(0)
        topview_player.load_frame(0)
        #----------------------------------------

        #display logic----------------------------
        #   add to loaded list
        #   load sprite frame
        #   manipulate changing size, position, frame loaded
        #   remove from loaded list
        #   set loaded frame to -1
        #-----------------------------------------

        propties.update_map((2,2))
        propties.has_control = True
        propties.game_style = 'topview'
        propties.city = 'city_1'

        #setup logic------------------------------
        #   update current map borders
        #   update whether the player has control or not
        #   update gamestyle/menu
        #   update current city (code_location)
        #   run the display logic given the current gamestyle and city
        #-----------------------------------------

        self._running = True

    def on_event(self,event):

        if event.type == pygame.QUIT:

            self._running = False

        if propties.has_control:

            if propties.is_topview():

                if event.type == pygame.KEYDOWN:

                    if event.key == K_LEFT:
                        propties.key_pressed[0] = True
                    elif event.key == K_UP:
                        propties.key_pressed[1] = True
                    elif event.key == K_DOWN:
                        propties.key_pressed[2] = True
                    elif event.key == K_RIGHT:
                        propties.key_pressed[3] = True

                elif event.type == pygame.KEYUP:

                    if event.key == K_LEFT:
                        propties.key_pressed[0] = False
                    elif event.key == K_UP:
                        propties.key_pressed[1] = False
                    elif event.key == K_DOWN:
                        propties.key_pressed[2] = False
                    elif event.key == K_RIGHT:
                        propties.key_pressed[3] = False

    def on_loop(self):

        if True in propties.key_pressed:

            keys = pygame.key.get_pressed()

            if propties.is_topview():

                if keys[K_LEFT]:

                    if topview_player.get_pos('x') <= 0.5 and\
                       propties.camera_offset[0] > propties.step[0]:
                        propties.camera_walk('-x')
                    elif topview_player.get_pos('x') >= 0:
                        topview_player.add_pos('x',-propties.step[0])

                if keys[K_UP]:

                    if topview_player.get_pos('y') <= 0.5 and\
                       propties.camera_offset[1] >= propties.step[1]:
                        propties.camera_walk('-y')
                    elif topview_player.get_pos('y') >= 0:
                        topview_player.add_pos('y',-propties.step[1])

                if keys[K_DOWN]:

                    if topview_player.get_pos('y') >= 0.5 and\
                       propties.camera_offset[1] <=\
                       propties.map_size[1]:
                        propties.camera_walk('+y')
                    elif topview_player.get_pos('y') <=\
                         1-topview_player.get_size('y'):
                        topview_player.add_pos('y',propties.step[1])

                if keys[K_RIGHT]:

                    if topview_player.get_pos('x') >= 0.5 and\
                       propties.camera_offset[0] <=\
                       propties.map_size[0]-propties.step[0]:
                        propties.camera_walk('+x')
                    elif topview_player.get_pos('x') <=\
                         1-topview_player.get_size('x'):
                        topview_player.add_pos('x',propties.step[0])

    def on_render(self):

        for sprite in static_sprites_bottom:

            if sprite.frame_loaded() != -1:

                sprite.render(self._gamescreen,self.size,\
                              propties.camera_offset)

        for sprite in player_sprites:

            if sprite.frame_loaded() != -1:

                sprite.render(self._gamescreen,self.size)

        for sprite in static_sprites_top:

            if sprite.frame_loaded() != -1:

                sprite.render(self._gamescreen,self.size,\
                              propties.camera_offset)

        for sprite in menu_sprites:

            if sprite.frame_loaded() != -1:

                sprite.render(self._gamescreen,self.size)

        pygame.display.flip()

    def on_cleanup(self):

        pygame.quit()

    def on_execute(self):

        if self.on_init() == False:
            self._running = False

        while(self._running):

            clock = pygame.time.Clock()
            clock.tick(60)

            for event in pygame.event.get():

                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def change_size(self,size):

        self.size = size
        self._gamescreen = pygame.display.set_mode(self.size)

if __name__ == "__main__":
    app = App()
    app.on_execute()
