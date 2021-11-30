"""Kruskals MST"""

from help import kruskal_help
from wiki import kruskal_wiki
from utils import *
import pygame
import sys
import math
import globals

# size = (width, height) = (640, 480)

(cols, rows) = (64 // 2, 48 // 2)


class Node:
    count = 0
    def __init__(self, pos):
        self.pos = pos
        self.number = Node.count
        Node.count += 1

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), self.pos, 10)


def length(n1, n2):
    return math.sqrt(math.pow(n1.pos[0] - n2.pos[0], 2)
                     + math.pow(n1.pos[1] - n2.pos[1], 2))


class Graph:
    def __init__(self):
        self.V = 1  # No. of vertices
        self.vertices = set()
        self.graph = []  # default dictionary


    def addEdge(
        self,
        u,
        v,
        w,
        pos_u,
        pos_v,
    ):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph.append([u, v, w, pos_u, pos_v])


    def find(self, parent, i):
        if parent[i]== i:
            return i
        return self.find(parent, parent[i])

    def union(
        self,
        parent,
        rank,
        x,
        y,
    ):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = [] 
        self.V = len(self.vertices)

        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            (u, v, w ,u_pos,v_pos) = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            if x != y:
                e = e + 1
                result.append([u, v, w,u_pos,v_pos])
                self.union(parent, rank, x, y)

        return result




def kruskal():
    global height,width
    pygame.init()
    win = pygame.display.set_mode(globals.size,pygame.RESIZABLE)
    pygame.display.set_caption("Kruskals MST")
    font = pygame.font.Font('freesansbold.ttf', 20)
    
        
    win.fill(MAIN_COL)


    g = Graph()
    vertices = []
    running_kruskal = True
    first = True
    while running_kruskal:
        globals.size = (width,height) = win.get_size()
        if first:
            n = Node((width // 2, height // 2))
            vertices.append(n)

            first = False

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if check_btn_collide(btns):
                    pass
                else:
                    pos = pygame.mouse.get_pos()
                    n_cur = Node(pos)
                    for n in vertices:
                        g.addEdge(u=n.number, v=n_cur.number, w=length(n,n_cur), pos_u=n.pos, pos_v=n_cur.pos)
                    vertices.append(n_cur)
            if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
                running_kruskal = False
            if keys[pygame.K_r]:
                g = Graph()
                vertices = []
                Node.count = 0
                n = Node((width // 2, height // 2))
                vertices.append(n)
        res = g.KruskalMST()

        for vertex in vertices:
            vertex.draw(win) 
         
        for edges in res:
            # pygame.draw.line(win, (0, 0, 0), edges[3],edges[4],width=4)
            pygame.draw.aaline(win, (0, 0, 0), edges[3],edges[4])
        
        draw_text(win,"Dynamic MST",(width//2,30,"center"),color=WHITE,font_size=28,bold=True)
        draw_text(win,f"Vertex count {g.V}",(width//2-10,height-50,"center"),color=WHITE,font_size=20,bold=True)

        button_1 = Button(win,"i",location=(50 ,height-50 ),action=kruskal_help,size=(40,30))
        button_2 = Button(win,"wiki",location=(width -100 ,height-50 ),action=kruskal_wiki,size=(80,30))
        
        btns = [button_1,button_2]

        
        for btn in btns:
            btn.draw()

        pygame.display.update()
        win.fill(MAIN_COL)


if __name__ == '__main__':
    kruskal()
