import pygame       #motor
import cnfig        #configuration variables
import sprts        #sprite class and groups
import texts        #dialogs
import sound        #sfx and music

#errors to fix:
#
#   when definition goes down and then back up the sprite loses quality
#       solution: reload image instead of transform
#
#things to improve:
#

class Game:

    def __init__(self):

        self._running = False
        self._screen = None
        self._size = self.width, self.height = cnfig.screen_size

    def on_init(self):

        pygame.init()
        pygame.display.set_caption('Last Raindrops')

        self._screen = pygame.display.set_mode(self._size)

        #temporal-----------------------------------
        sprts.logo_reteam.setup(sprts.bottom_passthrough_group)
        #-------------------------------------------

        self._running = True

    #if game lags, create:
    #
    #   load_radious = 1.5 screens
    #   add 'type' to sprites to sort them easily in their respective group
    #
    #   create_sprites = create sprites, .convert(), and .set_keycolor() them
    #   load_sprites = load sprites in a range load_radious
    #   unload_sprites = unload sprites further than load_radious

    def on_event(self,event):

        if event.type == pygame.QUIT:

            self._running = False

        if cnfig.has_control:

            if cnfig.game_mode == 'topview':

                if cnfig.can_move:

                    if event.type == pygame.KEYDOWN:

                        cnfig.recorded_inputs = [event.key] + cnfig.recorded_inputs

                        #temporal----------------------------------
                        if event.key == pygame.K_1:
                            self._screen = pygame.display.set_mode(self._size, pygame.FULLSCREEN)
                            cnfig.fullscreen = True
                        if event.key == pygame.K_2:
                            self.change_screen_size((1280, 720))
                        if event.key == pygame.K_3:
                            self.change_screen_size((1920, 1080))
                        if event.key == pygame.K_4:
                            self._screen = pygame.display.set_mode(self._size)
                            cnfig.fullscreen = False
                        if event.key == pygame.K_5:
                            self.change_screen_size((640, 360))
                        #------------------------------------------
                        #meme--------------------------------
                        if cnfig.recorded_inputs[5] == pygame.K_a:
                            if cnfig.recorded_inputs[4] == pygame.K_f:
                                if cnfig.recorded_inputs[3] == pygame.K_r:
                                    if cnfig.recorded_inputs[2] == pygame.K_i:
                                        if cnfig.recorded_inputs[1] == pygame.K_c:
                                            if cnfig.recorded_inputs[0] == pygame.K_a:
                                                sound.africa.play()
                        #------------------------------------

                        if event.key == pygame.K_LEFT:
                            cnfig.arrow_pressed = True
                            sprts.topview_player.facing = ['left'] + sprts.topview_player.facing
                        elif event.key == pygame.K_RIGHT:
                            cnfig.arrow_pressed = True
                            sprts.topview_player.facing = ['right'] + sprts.topview_player.facing
                        elif event.key == pygame.K_UP:
                            cnfig.arrow_pressed = True
                            sprts.topview_player.facing = ['up'] + sprts.topview_player.facing
                        elif event.key == pygame.K_DOWN:
                            cnfig.arrow_pressed = True
                            sprts.topview_player.facing = ['down'] + sprts.topview_player.facing

                        if cnfig.arrow_pressed:
                            sprts.topview_player.last_update = pygame.time.get_ticks()
                            cnfig.arrow_pressed = False

                    elif event.type == pygame.KEYUP:

                        if event.key == pygame.K_LEFT and 'left' in sprts.topview_player.facing:
                            sprts.topview_player.facing.remove('left')
                        elif event.key == pygame.K_RIGHT and 'right' in sprts.topview_player.facing:
                            sprts.topview_player.facing.remove('right')
                        elif event.key == pygame.K_UP and 'up' in sprts.topview_player.facing:
                            sprts.topview_player.facing.remove('up')
                        elif event.key == pygame.K_DOWN and 'down' in sprts.topview_player.facing:
                            sprts.topview_player.facing.remove('down')

    def on_loop(self):

        if cnfig.game_mode == 'reteam_logo':

            if cnfig.dummy_delay < 256:
                sprts.logo_reteam.image.set_alpha(cnfig.dummy_delay)
                cnfig.dummy_delay += 2

            elif cnfig.dummy_delay == 256:
                sprts.create_sprites()
                cnfig.dummy_delay +=1

            elif cnfig.dummy_delay < 300:
                cnfig.dummy_delay +=1

            else:
                cnfig.game_mode = 'topview'
                cnfig.has_control = True
                cnfig.dummy_delay = 0
                cnfig.can_move = True
                self.to_topview()

        sprts.player_group.update()
        sprts.menu_group.update()
        sprts.solid_group.update()
        sprts.top_passthrough_group.update()
        sprts.bottom_passthrough_group.update()

        if cnfig.new_screen_size != cnfig.screen_size:
            cnfig.screen_size = cnfig.new_screen_size

        cnfig.camera_move = (0, 0)

    def on_render(self):

        if cnfig.skipped_ticks > cnfig.ticks_to_skip:

            self._screen.fill((cnfig.bg_color))

            sprts.bottom_passthrough_group.draw(self._screen)
            sprts.solid_group.draw(self._screen)
            sprts.player_group.draw(self._screen)
            sprts.top_passthrough_group.draw(self._screen)
            sprts.menu_group.draw(self._screen)

            pygame.display.flip()

            cnfig.skipped_ticks = 0

        else: cnfig.skipped_ticks += 1

    def on_cleanup(self):

        pygame.quit()

    def on_execute(self):

        if self.on_init() == False:
            self._running = False

        clock = pygame.time.Clock()

        while self._running:

            clock.tick(60)

            #optional-----------------------------------
            tick_rate = clock.get_fps()
            if tick_rate < 45:
                cnfig.ticks_to_skip += 1
            elif tick_rate > 58 and cnfig.ticks_to_skip > 0:
                cnfig.ticks_to_skip -= 1
            #-------------------------------------------

            for event in pygame.event.get():

                    self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def change_screen_size(self,size):

        self._size = self.width, self.height = size
        if cnfig.fullscreen: self._screen = pygame.display.set_mode(self._size,pygame.FULLSCREEN)
        else: self._screen = pygame.display.set_mode(self._size)
        cnfig.new_screen_size = size

        scale = float(cnfig.new_screen_size[0]) / cnfig.screen_size[0]
        map_x = int(cnfig.map_size[0] * scale)
        map_y = int(cnfig.map_size[1] * scale)
        cnfig.map_size = map_x, map_y

    def to_topview(self):

        self.kill_sprites()

        sprts.topview_player.setup(sprts.player_group)
        sprts.example_tile_0.setup(sprts.bottom_passthrough_group)
        sprts.example_tile_1.setup(sprts.top_passthrough_group)
        sprts.example_tile_2.setup(sprts.solid_group)
        #sprts.map_main_city.setup(sprts.bottom_passthrough_group)
        #temporal------------------------
        texts.chat_box.setup(sprts.menu_group)
        #pygame.mixer.music.play(loops=-1)
        #--------------------------------

    def kill_sprites(self,group=None):

        if group == None:

            for sprite in sprts.bottom_passthrough_group: sprite.kill()
            for sprite in sprts.top_passthrough_group: sprite.kill()
            for sprite in sprts.solid_group: sprite.kill()
            for sprite in sprts.player_group: sprite.kill()
            for sprite in sprts.menu_group: sprite.kill()

        else:

            for sprite in group: sprite.kill()

if __name__ == '__main__':
    game = Game()
    game.on_execute()
