"""Kruskals MST"""


import pygame
import sys
from utils import *
import globals


def mm_help():
    pygame.init()
    win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
    pygame.display.set_caption("Help Menu")

    first = True
    font_size = globals.width//60

    running_help = True
    while running_help:

        if first:
            first = False
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                globals.size = (globals.width, globals.height) = event.size
                font_size = globals.width//60
                win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
                win.fill(BLACK)
            if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
                running_help = False

        win.fill(BLACK)

        text = '''
        ► To simulate any of the available click on it.
        ► To exit from any simulation press button 'q' on your keyboard.
        ► Once the simulation has finished press <ENTER> Key on your keyboard to return to main menu.
        ► Each simulation/demosntration will have its own help menu.
        '''

        render_textrect(win, text, (50, 80, globals.size[0]-80, globals.size[1]-200),
                        font_size=font_size, text_color=WHITE, background_color=BLACK, justification=0)

        draw_text(win, "Help Menu", pos=(
            (globals.size[0])//2, 50, "center"), color=WHITE, font_name="freesansbold.ttf", font_size=font_size*2)

        draw_text(win, "Press 'q' to exit Help", pos=(
            (globals.size[0])//2, globals.size[1]-100, "center"), font_size=font_size, color=WHITE)

        pygame.display.update()


def dijikstra_help():
    pygame.init()
    win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
    pygame.display.set_caption("Dijikstra Path Finder Help")

    first = True

    font_size = globals.width//60

    running_help = True
    while running_help:

        if first:
            first = False
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                globals.size = (globals.width, globals.height) = event.size
                font_size = globals.width//60
                win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
                win.fill(BLACK)
            if keys[pygame.K_q]:
                running_help = False

        win.fill(BLACK)

        text = '''
        ► Click on any cell to convert it into a Wall
        ► Hover on any cell while pressing down 'd' or left mouse button to remove wall from that cell.
        ► Click on any cell while pressing down 's' key to mark it as starting node
        ► Click on any cell while pressing down 'e' key to mark it as ending node
        ► Press <ENTER> to run the algorithm.
        ► Once the simulation has finished press <ENTER> Key on your keyboard to return to main menu.
        '''

        render_textrect(win, text, (50, 80, globals.size[0]-80, globals.size[1]-200),
                        font_size=font_size, text_color=WHITE, background_color=BLACK, justification=0)

        draw_text(win, "Dijikstra Help Menu", pos=(
            (globals.size[0])//2, 50, "center"), color=WHITE, font_name="freesansbold.ttf", font_size=font_size*2)

        draw_text(win, "Press 'q' to exit Help", pos=(
            (globals.size[0])//2, globals.size[1]-100, "center"), font_size=font_size, color=WHITE)
        pygame.display.update()


def kruskal_help():
    pygame.init()
    win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
    pygame.display.set_caption("Kruskals MST Finder Help")

    first = True

    font_size = globals.width//60

    running_help = True
    while running_help:

        if first:
            first = False
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                globals.size = (globals.width, globals.height) = event.size
                font_size = globals.width//60
                win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
                win.fill(BLACK)
            if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
                running_help = False

        win.fill(BLACK)

        text = '''
        ► Click anywhere on the screen to add a new node
        ► The algorithm will automatically include the added node and compute a minnimum spanning tree.
        ► Press key 'r' on keyboard to reset/clear the tree anytime
        ► You can press 'q' or '<ESC>' key anytime to exit the programm
        '''

        render_textrect(win, text, (50, 80, globals.size[0]-80, globals.size[1]-200),
                        font_size=font_size, text_color=WHITE, background_color=BLACK, justification=0)

        draw_text(win, "Kruskal Help Menu", pos=(
            (globals.size[0])//2, 50, "center"), color=WHITE, font_name="freesansbold.ttf", font_size=font_size*2)

        draw_text(win, "Press 'q' to exit Help", pos=(
            (globals.size[0])//2, globals.size[1]-100, "center"), font_size=font_size, color=WHITE)

        pygame.display.update()


def FFT_help():
    pygame.init()
    win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
    pygame.display.set_caption("Curve Compresser")

    first = True
    font_size = globals.width//60
    running_help = True
    while running_help:

        if first:
            first = False
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                globals.size = (globals.width, globals.height) = event.size
                font_size = globals.width//60
                win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
                win.fill(BLACK)
            if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
                running_help = False

        win.fill(BLACK)
        text = '''
        ► Draw any thing on the screen using your mouse while pressing right mouse button.
        ► You can change the number of points used for fitting the curve with the help of a dedicated slider in the bottom of screen.
        ► You can clear your drawing anytime by clicking clear button on the bottom right corner.
        ► You can press 'q' or '<ESC>' key anytime to exit the programm
        '''

        render_textrect(win, text, (50, 80, globals.size[0]-80, globals.size[1]-200),
                        font_size=font_size, text_color=WHITE, background_color=BLACK, justification=0)
        draw_text(win, "Curve Compresser Help Menu", pos=(
            (globals.size[0])//2, 50, "center"), color=WHITE, font_name="freesansbold.ttf", font_size=font_size*2)
        draw_text(win, "Press 'q' to exit Help", pos=(
            (globals.size[0])//2, globals.size[1]-100, "center"), font_size=font_size, color=WHITE)
        pygame.display.update()


def Astar_help():
    pygame.init()
    win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
    pygame.display.set_caption("Astar Path Finder Help")

    first = True

    font_size = globals.width//60

    running_help = True
    while running_help:

        if first:
            first = False
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                globals.size = (globals.width, globals.height) = event.size
                font_size = globals.width//60
                win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
                win.fill(BLACK)
            if keys[pygame.K_q]:
                running_help = False

        win.fill(BLACK)

        text = '''
        ► Click on any cell to convert it into a Wall
        ► Hover on any cell while pressing down 'd' or left mouse button to remove wall from that cell.
        ► Click on any cell while pressing down 's' key to mark it as starting node
        ► Click on any cell while pressing down 'e' key to mark it as ending node
        ► Press <ENTER> to run the algorithm.
        ► Once the simulation has finished press <ENTER> Key on your keyboard to return to main menu.
        '''

        render_textrect(win, text, (50, 80, globals.size[0]-80, globals.size[1]-200),
                        font_size=font_size, text_color=WHITE, background_color=BLACK, justification=0)

        draw_text(win, "Dijikstra Help Menu", pos=(
            (globals.size[0])//2, 50, "center"), color=WHITE, font_name="freesansbold.ttf", font_size=font_size*2)

        draw_text(win, "Press 'q' to exit Help", pos=(
            (globals.size[0])//2, globals.size[1]-100, "center"), font_size=font_size, color=WHITE)
        pygame.display.update()


def BubbleSort_help():
    pygame.init()
    win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
    pygame.display.set_caption("Bubble Sort Help")

    first = True

    font_size = globals.width//60

    running_help = True
    while running_help:

        if first:
            first = False
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                globals.size = (globals.width, globals.height) = event.size
                font_size = globals.width//60
                win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
                win.fill(BLACK)
            if keys[pygame.K_q]:
                running_help = False

        win.fill(BLACK)



        text = '''
        ► Change the number of elements to be sorted with the help of a dedicated slider in the bottom of screen.
        ► Press enter to run the Bubble Sort Alogrithm.
        ► Press <q> the quit the programm anytime.
        '''

        render_textrect(win, text, (50, 80, globals.size[0]-80, globals.size[1]-200),
                        font_size=font_size, text_color=WHITE, background_color=BLACK, justification=0)

        draw_text(win, "Bubble Sort Help Menu", pos=(
            (globals.size[0])//2, 50, "center"), color=WHITE, font_name="freesansbold.ttf", font_size=font_size*2)

        draw_text(win, "Press 'q' to exit Help", pos=(
            (globals.size[0])//2, globals.size[1]-100, "center"), font_size=font_size, color=WHITE)
        pygame.display.update()


if __name__ == '__main__':
    BubbleSort_help()
