import pygame
import random

step = 1
initial_options = [(0,step),(0,-step),(step,0),(-step,0)] * 1
choice_list = []
ticks = 1000
generation = 0
pygame.font.init()
font_arial = pygame.font.match_font('arial')
number_of_subjects = 20

for dummy in range(ticks):
    choice_list.append(initial_options)

def distance(sprite):
    global objective
    x = (sprite.rect.center[0]-objective.rect.center[0])**2
    y = (sprite.rect.center[1]-objective.rect.center[1])**2
    return x + y

class Subject(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((2,2))
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.center = (50,50)

        self.movements = []
        self.distance = distance(self)
        self.index = 0

    def update(self):

        movement = random.choice(choice_list[game._cnfig['counter']])

        new_y = self.rect.topleft[1] + movement[1]
        new_x = self.rect.topleft[0] + movement[0]
        self.rect.topleft = new_x, new_y

        collisions = pygame.sprite.spritecollide(self,obstacles,False)
        if collisions:
            new_y = self.rect.topleft[1] - movement[1]
            new_x = self.rect.topleft[0] - movement[0]
            self.rect.topleft = new_x, new_y

        self.movements.append(movement)

        if distance(self) < self.distance:
            self.distance = distance(self)
            self.index = game._cnfig['counter']

        collisions = pygame.sprite.spritecollide(self,goal,False)
        if collisions:
            game._cnfig['counter'] = ticks-1

class Obstacle(pygame.sprite.Sprite):

    def __init__(self,pos,size,color=(0,0,255)):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        pass

class Goal(pygame.sprite.Sprite):

    def __init__(self,pos,size,color=(0,0,255)):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        pass

class Game:

    def __init__(self):

        self._cnfig = {'fps':50,'screen_size':(512,512),'counter':0} #temporal

        self._running = False
        self._screen = None
        self._size = self.width, self.height = self._cnfig['screen_size']

    def on_init(self):

        pygame.init()
        pygame.display.set_caption('test')
        #pygame.display.set_icon()

        self._screen = pygame.display.set_mode(self._size)

        self._running = True

    def on_event(self,event):

        if event.type == pygame.QUIT:

            self._running = False

    def on_loop(self):

        obstacles.update()
        subjects.update()
        goal.update()

        global ticks

        if self._cnfig['counter'] == ticks-1:

            best_subject = Subject()

            for subject in subjects:

                if subject.distance < best_subject.distance:
                    best_subject = subject

                subject.kill()

            for index in range(best_subject.index):

                haha = best_subject.movements[index]
                choice_list[index].append(haha)
            global number_of_subjects
            for dummy in range(number_of_subjects):
                subjects.add(Subject())

            self._cnfig['counter'] = 0
            global generation
            generation += 1

        else: self._cnfig['counter'] += 1

    def on_render(self):
        self._screen.fill((0,0,0))
        subjects.draw(self._screen)
        obstacles.draw(self._screen)
        goal.draw(self._screen)

        global font_arial
        font = pygame.font.Font(font_arial,20)
        global generation
        image = font.render('current generation: '+str(generation), True, (255,0,0))
        self._screen.blit(image,(10,470))

        pygame.display.flip()

    def on_cleanup(self):

        pygame.quit()

    def on_execute(self):

        if self.on_init() == False:
            self._running = False

        clock = pygame.time.Clock()

        while self._running:

            #clock.tick(self._cnfig['fps'])

            for event in pygame.event.get():

                    self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

subjects = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
goal = pygame.sprite.Group()

objective = Goal(size=(20,20),pos=(300,400),color=(0,255,0))
goal.add(objective)

for dummy in range(number_of_subjects):
    subjects.add(Subject())

#obstacles.add(Obstacle(size=(200,20),pos=(40,200)))
#obstacles.add(Obstacle(size=(20,300),pos=(260,0)))

obstacles.add(Obstacle(size=(4,512),pos=(500,0),color=(0,0,0)))
obstacles.add(Obstacle(size=(500,4),pos=(0,500),color=(0,0,0)))
obstacles.add(Obstacle(size=(4,512),pos=(0,0),color=(0,0,0)))
obstacles.add(Obstacle(size=(500,4),pos=(0,0),color=(0,0,0)))

if __name__ == '__main__':
    game = Game()
    game.on_execute()
