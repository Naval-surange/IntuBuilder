from dijikstra import dijikstra
from Astar import AStar
from mst import kruskal
from fft import fft
from bubble_sort import bubble_sort
from insertionsort import InsertionSort
from convays import convays
from help import mm_help    

from utils import *

import globals
import pygame, sys

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Vizulizer Menu')    

screen = pygame.display.set_mode(globals.size,pygame.RESIZABLE)

font = pygame.font.SysFont(None, 50)


def set():
    global font
    font = pygame.font.SysFont(None, 50)
    pygame.display.set_caption('Vizulizer Menu')    



def run_dijikstra():
    dijikstra()
    set()
    
def run_AStar():
    AStar()
    set()
    
def run_fft():
    fft()
    set()
    
def run_kruskal():
    kruskal()
    set()
    
def run_bubble_sort():
    bubble_sort()
    set()
    
def run_insertion_sort():
    InsertionSort()
    set()
    
def run_convays():
    convays()
    set()


def main_menu():
    
    gifFrameList = loadGIF("./images/main_menu_bg.gif")
    currentFrame = 0
    
        
    while True:
        globals.size = (width, height) = screen.get_size()

        start_pos = height//2 - 200
        gap = 50
        button_1 = Button(screen,"Dijikstra",location=(width//2 ,start_pos ),action=run_dijikstra,size=(160,30))
        button_2 = Button(screen,"AStar",location=(width//2 ,start_pos+gap ),action=run_AStar,size=(160,30))
        button_3 = Button(screen,"Curve Compresser",location=(width//2 ,start_pos + 2*gap  ),action=run_fft,size=(160,30))
        button_4 = Button(screen,"Minimum Spanning Tree",location=(width//2 ,start_pos  +3*gap),action=run_kruskal,size=(240,30))
        button_5 = Button(screen,"Bubble Sort",location=(width//2 ,start_pos  +4*gap),action=run_bubble_sort,size=(160,30))
        button_6 = Button(screen,"Insertion Sort",location=(width//2 ,start_pos  +5*gap),action=run_insertion_sort,size=(160,30))
        button_7 = Button(screen,"Convays Game of Life",location=(width//2 ,start_pos  +6*gap),action=run_convays,size=(200,30))
        
        button_i = Button(screen,"i",location=(50 ,height-gap ),action=mm_help,size=(40,30))
        
        
        btns = [button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_i]

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_btn_collide(btns)

        screen.fill((44, 62, 80))
        
        rect = gifFrameList[currentFrame].get_rect(center = (width//2, height-100))
        screen.blit(gifFrameList[currentFrame], rect)
        currentFrame = (currentFrame + 1) % len(gifFrameList)
        
        draw_text(screen,"MAIN MENU",pos=(width//2,50,"center"),color=WHITE,font_name="freesansbold.ttf",font_size=45)
        for btn in btns:
            btn.draw()

        
        pygame.display.update()
        mainClock.tick(60)


main_menu()