from Sprite import *

#24 sprites in x
#14 sprites in y
#slightly bigger size to fill aproximation errors

#static_sprites_bottom: currently loaded background sprites
#player_sprites: currently loaded player sprite
#static_sprites_top: currently loaded sprites overlapping player
#menu_sprites: top sprites set to an specificic position on top of everything, cinematics

#sprite loading test----------------------
lol_haha = []
for i1 in range(48):
    for i2 in range(28):
        lol_haha.append(Sprite(['LR - pygame/resources/ground_0.png'],(i1/24.0,i2/14.0),(1.0/23,1.0/13),'static_bottom'))

topview_player = Sprite(['LR - pygame/resources/player.png'],(0,0),(1.0/23,1.0/13),'player')

#sprite loading test----------------------

static_sprites_bottom = []
player_sprites = []
static_sprites_top= []
menu_sprites = []
