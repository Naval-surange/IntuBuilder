from tkinter import EXCEPTION
from PIL.Image import TRANSPOSE
import pygame

from pygame.constants import K_RETURN

import globals
import sys
from utils import *


class Grid():
    def __init__(self, x, y) -> None:
        self.w = globals.size[0]//x
        self.h = globals.size[1]//y
        self.x = x
        self.y = y
        self.current = [[0 for i in range(y)] for j in range(x)]
        self.next = [[0 for i in range(y)] for j in range(x)]

    def draw(self, screen):
        for i in range(self.x):
            for j in range(self.y):
                if self.current[i][j] == 1:
                    pygame.draw.rect(
                        screen, GREY, (i*self.w, j*self.h, self.w-2, self.h-2))
                else:
                    pygame.draw.rect(screen, MAIN_COL,
                                     (i*self.w, j*self.h, self.w-2, self.h-2))

    def modify_cell(self, pos, state):
        i = pos[0] // self.w
        j = pos[1] // self.h
        try:
            self.current[i][j] = state
        except IndexError:
            pass

    def update_cell(self, x, y):
        count = self.current[x-1][y-1] + self.current[x-1][y] + self.current[x-1][y+1] + self.current[x][y - 1] + self.current[x][y+1] + self.current[x+1][y-1] + self.current[x+1][y] + self.current[x+1][y+1]
        if (self.current[x][y] == 1 and (count == 2 or count == 3) ):
            return 1
        elif(self.current[x][y] == 0 and count == 3):
            return 1
        else:
            return 0

    def update(self):
        # updates the cells of grid based on rules of convays game of life
        self.next = [[0 for i in range(self.y)] for j in range(self.x)]
        
        for i in range(1, self.x-1):
            for j in range(1, self.y-1):
                self.next[i][j] = self.update_cell(i, j)
        self.current = self.next


def convays():
    pygame.init()

    win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
    win.fill(BLACK)

    pygame.display.set_caption('Conveys Game of Life')
    clock = pygame.time.Clock()

    running_sim = True

    grd = Grid(51, 30)

    num_iter = 0
    cur_iter = 0
    
    box_len = 100
    inp = InputBox( 300 - box_len//2, globals.size[1] - 100, box_len, 50)
    
    while running_sim:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.VIDEORESIZE:
                globals.size = (globals.width, globals.height) = event.size
                win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
                win.fill(BLACK)
                grd = Grid(51, 30)
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running_sim = False
                elif event.key == pygame.K_SPACE:
                    num_iter += 1
                elif event.key == pygame.K_RETURN:
                    if inp.text.isnumeric():
                        num_iter = int(inp.text)
                        cur_iter = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if inp.rect.collidepoint(event.pos):
                    pass
                elif event.button in (1, 3):
                    grd.modify_cell(pygame.mouse.get_pos(), event.button == 1)

            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] or event.buttons[2]:
                    grd.modify_cell(pygame.mouse.get_pos(), event.buttons[0])

            inp.handle_event(event)
        
        if cur_iter <= num_iter:
            grd.update()
            cur_iter += 1
        
        win.fill(BLACK)
        grd.draw(win)


        inp.update()
        inp.draw(win)
        render_textrect(win,"ITERATIONS: ",(20,globals.size[1] - 100,200,50 ),justification=1,text_color=BLUE, font_size=34, background_color=COLOR_INACTIVE,font_name="Arial")
        # draw_text(win,"ITERATIONS : ",(20,globals.size[1]-75 , "left"),font_size=38,color=BLUE , font_name="freesansbold.ttf")
        
        clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    convays()
