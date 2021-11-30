"""Djikstra's Path Finding"""

from functools import partial
import pygame, sys


import globals

from collections import deque
from tkinter import  messagebox, Tk

from utils import *
from help import dijikstra_help
from wiki import dijikstra_wiki


cols, rows = 64//2, 48//2

w = globals.width//cols
h = globals.height//rows

grid = []
queue, visited = deque(), []
path = []

maze_loaded = False

class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j

        self.neighbors = []
        self.prev = None
        self.wall = 0
        self.visited = False
        
    def show(self, win, col, shape= 1):
        if self.wall == True:
            col = (0, 0, 0)
        if shape == 1:
            pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))
        else:
            pygame.draw.circle(win, col, (self.x*w+w//2, self.y*h+h//2), w//3)
    
    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])
        #Add Diagonals


def clickWall(pos, state):
    i = pos[0] // w
    j = pos[1] // h
    try:
        grid[i][j].wall = state
    except IndexError:
        pass


def load(grid):
    global cols,rows,w,h,maze_loaded
    maze_loaded = True
    file = open("grid.data","r")
    
    globals.size = (globals.width,globals.height) = tuple([int(s) for s in file.readline().split()])
    
    cols, rows = globals.width//28, globals.height//28
    w = globals.width//cols
    h = globals.height//rows
    
    grid.clear()
    
    
    for i in range(cols):
        arr = []
        for j in range(rows):
            arr.append(Spot(i, j))
        grid.append(arr)
        
    for i in range(cols):
        for j in range(rows):
            grid[i][j].add_neighbors(grid)
    
    pygame.display.set_mode(globals.size)
    
    for line in file.readlines():
        data_arr = [int(s) for s in line.split()]
        grid[data_arr[0]][data_arr[1]].wall = data_arr[2] 
        
    
def save(grid):
    global cols,rows
    file = open("grid.data","w")
    file.write(f"{globals.width} {globals.height}\n")
    for i in range(cols):
        for j in range(rows):
            spot = grid[i][j]
            file.write(f"{spot.x} {spot.y} {int(spot.wall)}\n")
    
def dijikstra():
    
    global cols,rows,w,h,maze_loaded
    
    pygame.init()

    win = pygame.display.set_mode(globals.size,pygame.RESIZABLE)
    pygame.display.set_caption("Dijktdtra's Path Finding")

    global grid,queue,visited,path
    grid = []
    queue, visited = deque(), []
    path = []

    
    running_dijikstra = True
    flag = False
    noflag = True
    startflag = False
    no_sol = False
    ready_to_exit = False

    
    prev_size =  (-1,-1)

    while running_dijikstra:
        globals.size = (globals.width, globals.height) = win.get_size() 
    
        if prev_size != globals.size:
            cols, rows = globals.width//28, globals.height//28
            w = globals.width//cols
            h = globals.height//rows    
            grid = []
            queue, visited = deque(), []
            path = []

            
            for i in range(cols):
                arr = []
                for j in range(rows):
                    arr.append(Spot(i, j))
                grid.append(arr)
                
            for i in range(cols):
                for j in range(rows):
                    grid[i][j].add_neighbors(grid)

            start = grid[5][5]
            start.wall = 0
            start.visited = True
            
            end = grid[cols- cols//4][rows//2]
            end.wall = 0

            queue.append(start)

            button_1 = Button(win,"i",location=(50 ,globals.height-50 ),action=dijikstra_help,size=(40,30))
            button_2 = Button(win,"wiki",location=(globals.width-100 ,globals.height-50 ),action=dijikstra_wiki,size=(80,30))   
            button_3 = Button(win,"Load Maze",location=(globals.width//2 ,globals.height-50 ),action=partial(load,grid),size=(160,30))   
                 
            prev_size = globals.size
            
         
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ready_to_exit and (keys[pygame.K_RETURN] or keys[pygame.K_q]) :
                running_dijikstra = False
            if keys[pygame.K_q]:
                running_dijikstra = False
                
            if keys[pygame.K_d] and not ready_to_exit:
                pos = pygame.mouse.get_pos()
                try:
                    grid[pos[0] // (globals.width // cols )][pos[1]//(globals.height//rows)].wall = False
                except IndexError:
                    pass
            elif keys[pygame.K_LCTRL]:
                if keys[pygame.K_s]:
                    save(grid)
                elif keys[pygame.K_l]:
                    load(grid)
            elif keys[pygame.K_s] and not startflag:
                start.visited = False
                pos = pygame.mouse.get_pos()
                try:
                    start = grid[pos[0] // (globals.width // cols )][pos[1]//(globals.height//rows)]
                    start.wall = 0
                    start.visited = True
                    queue.clear()
                    queue.append(start)
                except IndexError:
                    pass
            elif keys[pygame.K_e] and not startflag:
                pos = pygame.mouse.get_pos()
                try:
                    end = grid[pos[0] // (globals.width // cols )][pos[1]//(globals.height//rows)]
                    end.wall = 0
                except IndexError:
                    pass
            elif keys[pygame.K_l]:
                load(grid)
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_btn_collide([button_1,button_2,button_3])
                
            if not startflag:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button in (1, 3):  
                        clickWall(pygame.mouse.get_pos(), event.button==1)
                        
                elif event.type == pygame.MOUSEMOTION:
                    if event.buttons[0] or event.buttons[2]:
                        clickWall(pygame.mouse.get_pos(), event.buttons[0])
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if start.wall or end.wall:
                            Tk().wm_withdraw()
                            messagebox.showinfo("No start/end Node", "Add starting and ending node by pressing keys s and e on keyboard" )
                        else:
                            startflag = True


        if startflag:   #Dijikstra Algorithm
            if len(queue) > 0:
                current = queue.popleft()
                if current == end:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev 
                    if not flag:
                        flag = True
                        Tk().wm_withdraw()
                        messagebox.showinfo("Path found", "shortest path found!!" )
                        print("Done")
                        ready_to_exit = True
                    elif flag:
                        continue
                if flag == False:
                    for i in current.neighbors:
                        if not i.visited and not i.wall:
                            i.visited = True
                            i.prev = current
                            queue.append(i)
            else:
                if noflag and not flag:
                    noflag = False
                    no_sol = True
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution" )
                    ready_to_exit = True
                else:
                    continue


        win.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, (44, 62, 80))
                if spot in path:
                    spot.show(win, (46, 204, 113))
                    spot.show(win, (192, 57, 43), 0)
                elif spot.visited:
                    spot.show(win, (39, 174, 96))
                if spot in queue and not flag:
                    spot.show(win, (44, 62, 80))
                    spot.show(win, (39, 174, 96), 0)
                if spot == start:
                    spot.show(win, (0, 255, 200))
                if spot == end:
                    spot.show(win, (0, 120, 255))
            
        if not startflag:
            button_1.draw()
            button_2.draw()
            button_3.draw()

        
        if ready_to_exit:
            if flag:      
                draw_text(win,"Shortest Path Found !!",color=WHITE,pos=(globals.width//2,50,'center'),font_size=28,bold=True)
            if no_sol:
                draw_text(win,"No path found !!",color=RED,pos=(globals.width//2,50,'center'),font_size=28,bold=True)
                
            draw_text(win,"Press 'q' or '<ENTER>' to exit",color=WHITE,pos=(globals.width//2,globals.height-50,'center'),font_size=28,bold=True)
            
        pygame.display.update()


if __name__=="__main__":
    dijikstra()