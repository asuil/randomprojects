import os           #folder management

game_folder = os.path.dirname(__file__)

img_folder = os.path.join(game_folder, 'img')
sfx_folder = os.path.join(game_folder, 'sfx')

#bg_color = 5, 2, 8
screen_size = 1280, 720                     #2560, 1440; 1920, 1080; 1280, 720; 640, 360
new_screen_size = 1280, 720
game_mode = 'reteam_logo'
walk_step = 2
has_control = False
can_move = False
map_size = 1280, 720    #not used yet
camera_move = (0,0)
arrow_pressed = True
dummy_delay = 0
recorded_inputs = [None,None,None,None,None,None]
regular_sprite_size = 64, 64
bg_color = 5,2,8
text_speed = 5
skipped_ticks = 0       #render-only
ticks_to_skip = 0       #render-only
fullscreen = False
