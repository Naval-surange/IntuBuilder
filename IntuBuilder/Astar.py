from functools import partial
import pygame, sys, math
import globals

from tkinter import messagebox, Tk
from utils import Button, check_btn_collide
from wiki import AStar_wiki
from help import Astar_help
# from help import 


cols, rows = 64//2, 48//2


grid = []
openSet, closeSet = [], []
path = []

w = globals.width//cols
h = globals.height//rows

class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        # if random.randint(0, 100) < 20:
        #     self.wall = True
        
    def show(self, win, col):
        if self.wall == True:
            col = (0, 0, 0)
        pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))
    
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
        if self.x < cols - 1 and self.y < rows - 1:
            self.neighbors.append(grid[self.x+1][self.y+1])
        if self.x < cols - 1 and self.y > 0:
            self.neighbors.append(grid[self.x+1][self.y-1])
        if self.x > 0 and self.y < rows - 1:
            self.neighbors.append(grid[self.x-1][self.y+1])
        if self.x > 0 and self.y > 0:
            self.neighbors.append(grid[self.x-1][self.y-1])


def clickWall(pos, state):
    i = pos[0] // w
    j = pos[1] // h
    grid[i][j].wall = state

def place(pos):
    i = pos[0] // w
    j = pos[1] // h
    return w, h
            
def heuristics(a, b):
    return math.sqrt((a.x - b.x)**2 + abs(a.y - b.y)**2)


def load(grid):
    global cols,rows,w,h

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


def close():
    pygame.quit()
    sys.exit()


def AStar():
    global grid,openSet,closeSet,path,cols,rows,w,h
    pygame.init()

    win = pygame.display.set_mode(globals.size,pygame.RESIZABLE)
    pygame.display.set_caption('AStar Path finding')

    clock = pygame.time.Clock()
    fps = 30

    
    
    prev_size = (-1,-1)
    

    flag = False
    noflag = True
    startflag = False
    running_AStar = True
    ready_to_exit = False
    
    while running_AStar:
        
        globals.size = (globals.width, globals.height) = win.get_size()
        if globals.size != prev_size:
            
            cols, rows = globals.width//28, globals.height//28
            w = globals.width//cols
            h = globals.height//rows    
            
            grid = []
            openSet, closeSet = [], []
            path = []
            for i in range(cols):
                arr = []
                for j in range(rows):
                    arr.append(Spot(i, j))
                grid.append(arr)
            
            for i in range(cols):
                for j in range(rows):
                    grid[i][j].add_neighbors(grid)

            start = grid[cols - cols//2][5]
            end = grid[cols - cols//2][rows - cols//4]

            openSet.append(start)
            
            
            button_1 = Button(win,"i",location=(50 ,globals.height-50 ),action=Astar_help,size=(40,30))
            button_2 = Button(win,"wiki",location=(globals.width-100 ,globals.height-50 ),action=AStar_wiki,size=(80,30))
            button_3 = Button(win,"Load Maze",location=(globals.width//2 ,globals.height-50 ),action=partial(load,grid),size=(160,30))   
            
            btns = [button_1,button_2,button_3]

            prev_size = globals.size
        
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ready_to_exit and keys[pygame.K_RETURN]:
                running_AStar = False
            if keys[pygame.K_q]:
                running_AStar = False

            if keys[pygame.K_d]:
                pos = pygame.mouse.get_pos()
                grid[pos[0] // (globals.width // cols )][pos[1]//(globals.height//rows)].wall = False 
            elif keys[pygame.K_s]:
                        pos = pygame.mouse.get_pos()
                        start = grid[pos[0] // (globals.width // cols )][pos[1]//(globals.height//rows)]
                        start.wall = False
                        start.visited = True
                        openSet.clear()
                        openSet.append(start)
            elif keys[pygame.K_e]:
                pos = pygame.mouse.get_pos()
                end = grid[pos[0] // (globals.width // cols )][pos[1]//(globals.height//rows)]
                end.wall = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_btn_collide(btns)
                continue
            if not startflag:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button in (1, 3):  
                        clickWall(pygame.mouse.get_pos(), event.button==1)
                    
                elif event.type == pygame.MOUSEMOTION:
                    if event.buttons[0] or event.buttons[2]:
                        clickWall(pygame.mouse.get_pos(), event.buttons[0])
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        startflag = True

        if startflag:   #AStar algorithm
            if len(openSet) > 0:
                winner = 0
                for i in range(len(openSet)):
                    if openSet[i].f < openSet[winner].f:
                        winner = i

                current = openSet[winner]
                
                if current == end:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev 
                    if not flag:
                        flag = True
                        Tk().wm_withdraw()
                        messagebox.showinfo("Path found", "Path found!!" )
                        print("Done")
                        ready_to_exit = True
                    elif flag:
                        continue

                if flag == False:
                    openSet.remove(current)
                    closeSet.append(current)

                    for neighbor in current.neighbors:
                        if neighbor in closeSet or neighbor.wall:
                            continue
                        tempG = current.g + 1

                        newPath = False
                        if neighbor in openSet:
                            if tempG < neighbor.g:
                                neighbor.g = tempG
                                newPath = True
                        else:
                            neighbor.g = tempG
                            newPath = True
                            openSet.append(neighbor)
                        
                        if newPath:
                            neighbor.h = heuristics(neighbor, end)
                            neighbor.f = neighbor.g + neighbor.h
                            neighbor.prev = current

            else:
                if noflag:
                    noflag = False
                    ready_to_exit = True 
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution" )
                   

        win.fill((0, 20, 20))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, (44, 62, 80))
                if flag and spot in path:
                    spot.show(win, (25, 120, 250))
                elif spot in closeSet:
                    spot.show(win, (255, 0, 0))
                elif spot in openSet:
                    spot.show(win, (0, 255, 0))
                try:
                    if spot == end:
                        spot.show(win, (0, 120, 255))
                except Exception:
                    pass
        for btn in btns:
            btn.draw()
        clock.tick(fps)
        pygame.display.flip()



if __name__=="__main__":
    AStar()