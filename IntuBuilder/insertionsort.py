import pygame
import sys
import random
import time

from utils import *
import globals
pygame.init()

# size = (globals.width, globals.height) = 640, 480


x = 70
y = 80
z = 30
w = 20


def show(win, height, colors):
    global w, x, y
    pygame.draw.rect(win, MAIN_COL, pygame.Rect(
        0, y, globals.width, globals.height-140))

    for i in range(len(height)):
        pygame.draw.rect(win, colors[i], (x + z * i, y, w, height[i]))


def InsertionSort():
    global w, x, y, z
    op_count = 0
    delay = 50
    win = pygame.display.set_mode(globals.size, pygame.RESIZABLE)
    pygame.display.set_caption("Insertion sort")
    running_sort = True
    length = Slider(win, "Array Length", 10, 10, 50,
                    (globals.width//2-globals.width//3, globals.height-60))
    sliders = [length]
    size_arr = globals.width//w - 8
    values = [200, 50, 130, 90, 250, 61, 110,
              88, 33, 80, 70, 159, 180, 20]

    prev_size = (-1, -1)

    first = True
    startflag = False

    while running_sort:

        if first:
            win.fill(MAIN_COL)
            first = False

        size_n = int(length.val)

        globals.size = (globals.width, globals.height) = (
            globals.width, globals.height) = win.get_size()
        if prev_size != globals.size:
            win.fill(MAIN_COL)
            size_arr = size_n
            w = (globals.width - 100)//(size_n*2)
            z = (globals.width - 100)//(size_n)
            delay = int(500/size_arr)
            pygame.draw.rect(win, MAIN_COL, pygame.Rect(
                0, y, globals.width, globals.height-y))
            values = [random.randint(10, globals.height-150)
                      for _ in range(size_arr)]
            colors = [RED for _ in range(size_arr)]
            length = Slider(win, "Array Length", 10, 10, 50,
                            (globals.width//2-globals.width//3, globals.height-60))
            sliders = [length]

            show(win, values, colors)
            pygame.display.update()
            prev_size = globals.size

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_q]:
                running_sort = False
            if keys[pygame.K_RETURN]:
                startflag = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check_btn_collide(btns)
                pos = pygame.mouse.get_pos()
                for s in sliders:
                    if s.button_rect.collidepoint(pos):
                        s.hit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for s in sliders:
                    s.hit = False

        draw_text(win, "Insertion Sort", (globals.width//2,
                                          30, "center"), color=WHITE, font_size=30)

        if not startflag:
            size_n = int(length.val)
            if size_n != size_arr:
                size_arr = size_n
                w = (globals.width - 100)//(size_n*2)
                z = (globals.width - 100)//(size_n)
                delay = int(500/size_arr)
                pygame.draw.rect(win, MAIN_COL, pygame.Rect(
                    0, y, globals.width, globals.height-y))
                values = [random.randint(10, globals.height-150)
                          for _ in range(int(size_arr))]
                colors = [RED for _ in range(size_arr)]

                show(win, values, colors)
                pygame.display.update()

        for s in sliders:
            if s.hit:
                s.move()

        for s in sliders:
            s.draw()

        # for btn in btns:
        # 	btn.draw()

        pygame.display.update()

        if startflag:
            s_n_i = 1
            s_n = 1

            # code for insertion sort

            for i in range(1, size_arr):
                key = values[i]
                j = i-1
                while j >= 0 and values[j] > key:
                    for event in pygame.event.get():
                        keys = pygame.key.get_pressed()
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if keys[pygame.K_q]:
                            running_sort = False

                    values[j+1] = values[j]
                    j -= 1

                    values[j+1] = key
                    for k in range(size_arr):
                        colors[k] = RED
                    colors[j+1] = GREEN
                    show(win, values, colors)

                    op_count += 1

                    pygame.draw.rect(win, MAIN_COL, pygame.Rect(
                        globals.width//2-30, globals.height-50, 400, 80))

                    draw_text(win, f"Length Of array = {size_arr}", (
                        globals.width//2-30, globals.height-50, "left"), color=WHITE, font_size=20)
                    draw_text(win, f"Number of operations = {op_count}", (
                        globals.width//2-30, globals.height-25, "left"), color=WHITE, font_size=20)

                    string = "Sorting" + ("." * (s_n % 5))
                    s_n_i += 1
                    if not s_n_i % 5:
                        s_n += 1
                    pygame.draw.rect(win, MAIN_COL, pygame.Rect(
                        globals.width//2-globals.width//3-80, globals.height-100-50, 160, 80))
                    draw_text(win, string, pos=(globals.width//2-globals.width //
                                                3-50, globals.height-100, "left"), font_size=26, color=RED)

                    show(win, values, colors)
                    pygame.time.delay(delay)
                    pygame.display.update()
                    time.sleep(0.5/len(values))

            pygame.draw.rect(win, MAIN_COL, pygame.Rect(
                globals.width//2-globals.width//3-80, globals.height-100-50, 160, 80))
            draw_text(win, "Sorted!!", pos=(globals.width//2-globals.width //
                                            3, globals.height-100, "center"), font_size=26, color=GREEN)
            op_count = 0
            startflag = False


if __name__ == "__main__":
    InsertionSort()
