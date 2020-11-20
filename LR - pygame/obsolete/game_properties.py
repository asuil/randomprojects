#GameProperties:
#
#   has_control(bool): True if the player inputs will be processed
#   camera_offset(tuple(float)): camera position in game screen units
#   game_style(str): gamestyle to aply
#   key_pressed(list(bool)): list of the pressed value of movement arrows
#   step(tuple(float)): movement step (top view) in game screen units
#   map_size(tuple(float)): borders for the movement in game screen units
#   city(str): name of the loaded city
#   screen_size(tuple(int)): size of the screen in pixels (resolution)

step = (1.0/24/4, 1.0/14/4)
offset = (0,0)

class GameProperties:

    def __init__(self):

        self.has_control = None                  #bool
        self.camera_offset = (None,None)         #float, float
        self.game_style = None                   #topview,
        self.key_pressed = [None,None,None,None] #left, up, down, right
        self.step = (None,None)                  #float, float
        self.map_size = (None,None)              #float, float
        self.city = None                         #str
        self.screen_size = (None,None)           #int,int

    def is_topview(self):
        return self.game_style == 'topview'

    def camera_walk(self,coord):

        if coord == '+x':
            self.camera_offset = (self.camera_offset[0]+self.step[0],self.camera_offset[1])
        elif coord == '+y':
            self.camera_offset = (self.camera_offset[0],self.camera_offset[1]+self.step[1])
        elif coord == '-x':
            self.camera_offset = (self.camera_offset[0]-self.step[0],self.camera_offset[1])
        elif coord == '-y':
            self.camera_offset = (self.camera_offset[0],self.camera_offset[1]-self.step[1])

    def update_map(self,size):
        import Sprite
        map_size_0 = size[0]-1
        map_size_1 = size[1]-1
        self.map_size = (map_size_0,map_size_1)

propties = GameProperties()
propties.has_control = False
propties.camera_offset = offset
propties.game_style = None
propties.key_pressed = [False,False,False,False]
propties.step = step
propties.map_size = (None,None)
propties.city = None
propties.screen_size = (640, 360)
