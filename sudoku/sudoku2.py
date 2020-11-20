import tkinter as tk
import pygame
from s_36.classes import Sudoku
import os

root = tk.Tk()
root.overrideredirect(True)
embed = tk.Frame(root, width=0, height=0)
embed.pack()
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
root.update()

class Main:

    def __init__(self):

        self._running = False
        self._screen = None

        self._size = (600,450)
        self._name = "Sudoku Solver"
        self._bgcolor = (0,0,0)
        self._fps = 60

        self._bg = "image haha"
        self._selected = ()
        self._square = "image haha"

        self._raw_sudoku = {}
        for x in range(9):
            for y in range(9):
                self._raw_sudoku[(x,y)] = [1,2,3,4,5,6,7,8,9]

        self._sudoku = Sudoku(self._raw_sudoku)

        self._start = False

        self._screen_pos = (500, 225)
        self._may_move = False
        self._may_move_from = (0,0)

    def on_init(self):

        root.geometry("+"+str(self._screen_pos[0])+"+"+str(self._screen_pos[1]))
        embed.config(width=600,height=450)

        pygame.init()
        pygame.display.set_caption(self._name)
        #pygame.display.set_icon(self._cnfig.icon)

        self._screen = pygame.display.set_mode(self._size, pygame.NOFRAME)
        self._running = True

        self._bg = pygame.image.load("C:\\Users\\Ariel\\AppData\\Local\\Programs\\Python\\Python36-32\\s_36\\sudoku\\sudokubg.png").convert()

        self._square = pygame.Surface((49,49))
        self._square.fill((128,128,128))
        self._square.set_alpha(128)

    def on_event(self,event):

        if event.type == pygame.MOUSEMOTION and self._may_move:

            mouse_pos = pygame.mouse.get_pos()

            dx = mouse_pos[0] - self._may_move_from[0]
            dy = mouse_pos[1] - self._may_move_from[1]

            self._screen_pos = (self._screen_pos[0] + dx, self._screen_pos[1] + dy)

            screen_full_size = pygame.display.list_modes()[0]
            root.geometry("+"+str(self._screen_pos[0])+"+"+str(self._screen_pos[1]))

        elif event.type == pygame.MOUSEBUTTONUP:
            self._may_move = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            if pos[0] > 450:
                self._selected = ()

                if pos[0] > 470 and pos[0] < 585:

                    if pos[1] > 204 and pos[1] < 245:
                        self._start = True

                    elif pos[1] > 255 and pos[1] < 296:
                        self._raw_sudoku = {}
                        for x in range(9):
                            for y in range(9):
                                self._raw_sudoku[(x,y)] = [1,2,3,4,5,6,7,8,9]

                if pos[1] > 29 and pos[1] < 58:

                    if pos[0] > 546 and pos[0] < 575:
                        self._running = False

                    if pos[0] > 507 and pos[0] < 537:
                        self._may_move = True
                        self._may_move_from = pygame.mouse.get_pos()

            else:
                self._selected = int((pos[0]-1)/50), int((pos[1]-1)/50)

        elif event.type == pygame.KEYDOWN:

            if self._selected != ():

                numbers = range(49,59)
                for key in numbers:
                    if event.key == key:
                        self._raw_sudoku[self._selected] = [key - 48]
                if event.key == pygame.K_0 and self._selected in self._raw_sudoku:
                    self._raw_sudoku[self._selected] = [1,2,3,4,5,6,7,8,9]

                elif event.key == pygame.K_UP and self._selected[1] > 0:
                    self._selected = (self._selected[0], self._selected[1] - 1)
                elif event.key == pygame.K_DOWN and self._selected[1] < 8:
                    self._selected = (self._selected[0], self._selected[1] + 1)
                elif event.key == pygame.K_LEFT and self._selected[0] > 0:
                    self._selected = (self._selected[0] - 1, self._selected[1])
                elif event.key == pygame.K_RIGHT and self._selected[0] < 8:
                    self._selected = (self._selected[0] + 1, self._selected[1])

                #test
                elif event.key == pygame.K_t:
                    print(self._raw_sudoku[self._selected])

    def on_loop(self):

        self._sudoku = Sudoku(self._raw_sudoku)

        while self._start:

            for x in range(9):
                for y in range(9):

                    pos = (x,y)
                    to_remove = []

                    for value in self._sudoku.get_values(pos):
                        for cell in self._sudoku.get_impact(pos):
                            if cell == [value]:
                                to_remove.append([pos,value])
                                break

                    for set in to_remove:
                        pos = set[0]
                        value = set[1]
                        self._sudoku.remove(pos,value)

            for row in range(9):
                for value in [1,2,3,4,5,6,7,8,9]:
                    self._sudoku.get_row(row)

            for x in range(9):
                for y in range(9):
                    pos = (x,y)
                    values = self._sudoku.get_values(pos)
                    if len(values) == 1:
                        self._raw_sudoku[pos] = values

            self._start = False

    def on_render(self):

        self._screen.fill(self._bgcolor)
        self._screen.blit(self._bg, (0,0))
        if self._selected != ():
            self._screen.blit(self._square, (self._selected[0]*50+1, self._selected[1]*50+1))

        for pos in self._raw_sudoku:
            #could optimize
            if len(self._raw_sudoku[pos]) == 1:
                image = pygame.image.load("s_36\\sudoku\\" + str(self._raw_sudoku[pos][0]) + ".png")
                self._screen.blit(image, (pos[0]*50+1, pos[1]*50+1))

        pygame.display.flip()

    def on_cleanup(self):

        pygame.quit()

    def on_execute(self):

        if self.on_init() == False:
            self._running = False

        clock = pygame.time.Clock()
        while self._running:
            clock.tick(self._fps)

            for event in pygame.event.get():
                    self.on_event(event)

            self.on_loop()
            self.on_render()

            root.update()

        self.on_cleanup()

if __name__ == '__main__':
    solver = Main()
    solver.on_execute()
